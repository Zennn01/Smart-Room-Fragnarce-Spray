document.addEventListener('DOMContentLoaded', () => {
    // Theme Switch
    const themeSwitch = document.getElementById('themeSwitch');
    const body = document.body;
    
    // Check local storage for theme preference
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark') {
        body.classList.add('dark-theme');
        themeSwitch.textContent = '☀️';
    }

    themeSwitch.addEventListener('click', () => {
        body.classList.toggle('dark-theme');
        let theme = body.classList.contains('dark-theme') ? 'dark' : 'light';
        themeSwitch.textContent = theme === 'dark' ? '☀️' : '🌙';
        localStorage.setItem('theme', theme);
    });

    // Ripple Effect
    const addRipple = (e, button) => {
        const x = e.clientX - button.getBoundingClientRect().left;
        const y = e.clientY - button.getBoundingClientRect().top;
        
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        ripple.style.left = `${x}px`;
        ripple.style.top = `${y}px`;
        
        button.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
    };

    document.querySelectorAll('.ripple-btn').forEach(button => {
        button.addEventListener('click', function(e) { addRipple(e, this); });
    });

    // Sync Time to ESP32 on load
    fetch('/api/sync_time', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ timestamp: Math.floor(Date.now() / 1000) })
    }).catch(e => console.error('Time sync failed', e));

    // Elements
    const statusText = document.getElementById('status');
    const wifiStatus = document.getElementById('wifi');
    const deviceId = document.getElementById('deviceId');
    const deviceStatus = document.getElementById('deviceStatus');
    const connectionDot = document.getElementById('connectionDot');
    
    const infoDeviceName = document.getElementById('infoDeviceName');
    const infoIpAddress = document.getElementById('infoIpAddress');
    const infoRssi = document.getElementById('infoRssi');
    const infoVersion = document.getElementById('infoVersion');
    const activityList = document.getElementById('activityList');

    const modeManual = document.getElementById('modeManual');
    const modeAuto = document.getElementById('modeAuto');
    
    const sprayDuration = document.getElementById('sprayDuration');
    const scheduleStart = document.getElementById('scheduleStart');
    const scheduleEnd = document.getElementById('scheduleEnd');
    const scheduleInterval = document.getElementById('scheduleInterval');
    const saveScheduleBtn = document.getElementById('saveScheduleBtn');

    // Polling Status
    let isConnected = false;

    function updateUI(data) {
        if (!isConnected) {
            isConnected = true;
            connectionDot.classList.add('connected');
            deviceStatus.textContent = 'Device Connected';
            wifiStatus.textContent = data.connection;
            document.getElementById('connectBtn').style.display = 'none'; // Hide connect button since it's real
        }

        statusText.textContent = data.status;
        deviceId.textContent = data.device_name;
        
        infoDeviceName.textContent = data.device_name;
        infoIpAddress.textContent = data.ip_address;
        infoRssi.textContent = data.rssi;
        infoVersion.textContent = data.version;

        // Update Mode buttons silently (without triggering API call)
        if (data.mode === 'manual') {
            modeManual.classList.add('active');
            modeAuto.classList.remove('active');
        } else {
            modeAuto.classList.add('active');
            modeManual.classList.remove('active');
        }

        // Update Schedule (only if not currently focused to avoid annoying user)
        if (document.activeElement !== scheduleStart) scheduleStart.value = data.schedule.start;
        if (document.activeElement !== scheduleEnd) scheduleEnd.value = data.schedule.end;
        if (document.activeElement !== scheduleInterval) scheduleInterval.value = data.schedule.interval;
        if (document.activeElement !== sprayDuration) sprayDuration.value = data.duration;

        // Update History
        activityList.innerHTML = '';
        data.history.forEach(item => {
            const li = document.createElement('li');
            li.innerHTML = `<span>✔ ${item.mode} (${item.duration}s)</span><span>${item.time}</span>`;
            activityList.appendChild(li);
        });
    }

    async function fetchStatus() {
        try {
            const response = await fetch('/api/status');
            if (response.ok) {
                const data = await response.json();
                updateUI(data);
            } else {
                throw new Error("HTTP error " + response.status);
            }
        } catch (error) {
            // Mock data for Live Server development
            if (location.hostname === '127.0.0.1' || location.hostname === 'localhost') {
                const mockData = {
                    status: "Ready (Mock)",
                    connection: "Local Server",
                    device_name: "ESP-Mock-01",
                    ip_address: "127.0.0.1",
                    rssi: "-40 dBm",
                    version: "v1.0-mock",
                    mode: "manual",
                    duration: 3,
                    schedule: { start: "08:00", end: "20:00", interval: 60 },
                    history: [{ mode: "Manual Spray", duration: 3, time: "10:00" }]
                };
                updateUI(mockData);
                return;
            }

            console.error('Error fetching status:', error);
            if (isConnected) {
                isConnected = false;
                connectionDot.classList.remove('connected');
                deviceStatus.textContent = 'Device Not Connected';
                wifiStatus.textContent = 'Offline';
                document.getElementById('connectBtn').style.display = 'inline-block';
            }
        }
    }

    setInterval(fetchStatus, 2000);
    fetchStatus();

    // Mode Toggle
    async function setMode(mode) {
        try {
            await fetch('/api/mode', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mode: mode })
            });
            fetchStatus(); // immediate refresh
        } catch(e) { console.error(e); }
    }

    modeManual.addEventListener('click', () => setMode('manual'));
    modeAuto.addEventListener('click', () => setMode('automatic'));

    // Duration Change
    sprayDuration.addEventListener('change', async (e) => {
        try {
            await fetch('/api/duration', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ duration: parseInt(e.target.value) })
            });
        } catch(e) { console.error(e); }
    });

    // Save Schedule
    saveScheduleBtn.addEventListener('click', async () => {
        const schedule = {
            start: scheduleStart.value,
            end: scheduleEnd.value,
            interval: parseInt(scheduleInterval.value)
        };
        try {
            const oldText = saveScheduleBtn.textContent;
            saveScheduleBtn.textContent = 'Saving...';
            await fetch('/api/schedule', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(schedule)
            });
            setTimeout(() => { saveScheduleBtn.textContent = oldText; }, 1000);
        } catch(e) { console.error(e); }
    });

    // Spray Button
    const sprayButton = document.getElementById('sprayButton');

    sprayButton.addEventListener('click', async function(e) {
        if (!isConnected) {
            alert("Waiting for connection to device...");
            return;
        }
        
        // Spray Animation
        const rect = this.getBoundingClientRect();
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        for (let i = 0; i < 15; i++) {
            createParticle(this, centerX, centerY);
        }

        try {
            statusText.textContent = 'Spraying...';
            await fetch('/api/spray', { method: 'POST' });
            fetchStatus(); // refresh UI
        } catch(e) { console.error(e); }
    });

    function createParticle(parent, x, y) {
        const particle = document.createElement('div');
        particle.classList.add('spray-particle');
        
        const angle = Math.random() * Math.PI * 2;
        const distance = 50 + Math.random() * 50;
        const tx = Math.cos(angle) * distance;
        const ty = Math.sin(angle) * distance - 80;
        
        particle.style.left = `${x}px`;
        particle.style.top = `${y}px`;
        particle.style.setProperty('--tx', `${tx}px`);
        particle.style.setProperty('--ty', `${ty}px`);
        
        parent.appendChild(particle);
        
        particle.style.animation = `sprayEffect ${0.5 + Math.random() * 0.5}s ease-out forwards`;
        
        setTimeout(() => {
            particle.remove();
        }, 1000);
    }
});
