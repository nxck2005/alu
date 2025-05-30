document.addEventListener('DOMContentLoaded', function() {
    console.log("hello, world")

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