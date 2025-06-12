document.addEventListener('DOMContentLoaded', function() {
    console.log("Page loaded")

    let startupTime;

    // just to make it clear to me lol sorry
    const SECONDS_PER_DAY = 86400;
    const SECONDS_PER_HOUR = 3600;
    const SECONDS_PER_MINUTE = 60;

    // fetch startup time only once, we'll calculate uptime client side
    fetch('/hStatus')
        .then(response => response.json())
        .then(data => {
            startupTime = new Date(data.startupTime);
            document.getElementById('startuptime').textContent = `${startupTime.toLocaleString()}`;;
            updateUptime();
        });

    function updateUptime() {
        if (!startupTime) return;

        const now = new Date();
        const uptimeMs = now - startupTime;
        const uptimeS = Math.floor(uptimeMs / 1000)

        const days = Math.floor(uptimeS / SECONDS_PER_DAY);
        const hours = Math.floor((uptimeS % SECONDS_PER_DAY) / SECONDS_PER_HOUR);
        const minutes = Math.floor((uptimeS % SECONDS_PER_HOUR) / SECONDS_PER_MINUTE);
        const leftoverSeconds = uptimeS % SECONDS_PER_MINUTE

        document.getElementById('uptime').textContent =
        `${days}d ${hours}h ${minutes}m ${leftoverSeconds}s`
    }

    setInterval(updateUptime, 1000)
    
    const execButton = document.getElementById("execbutton")
    const pokeAluButton = document.getElementById("pokealubutton")
    const pokeMemButton = document.getElementById("pokemembutton")
    const resetalubutton = document.getElementById("resetalubutton")
    const resetmembutton = document.getElementById("resetmembutton")

    const hexInputs = document.querySelectorAll('#pokeval, #rowval');

    // validate hex inputs real time
    hexInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            const value = e.target.value.replace(/[^0-9A-Fa-f]/g, '');
            e.target.value = value.toUpperCase();
        })
    })    
})