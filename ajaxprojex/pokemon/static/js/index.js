$.ajax({
    url: '/all_pokemon',
    type: "GET",
    success: function(data) {
        console.log(data);
    }
})

$(document).ready(function(){
    var teamOfSix = [];
    $('.poke').on('click', function () {
        $('#team').html("");
            for (var i = 0; i < 6; i++) {
                var pokeResponse, pokemon = {};
                var ran = Math.floor((Math.random() * 719) + 2);
                var imageURL = 'http://pokeapi.co';
                        $.ajax({
                            url: "http://pokeapi.co/api/v1/sprite/" + ran + "/",
                            type: "GET",
                            dataType: "jsonp",
                            success: function (data) {
                                pokeResponse = data;
                                pokemon.name = data.pokemon.name;
                                pokemon.id = data.id - 1;
                                pokemon.image = data.image;
                                $('#team').append("<img class='pokemon' src=" + imageURL + pokemon.image + "/>");
                                teamOfSix.push(pokeResponse);
                                }
                    });
            }
     });
    $('.createandsaveteam').on('click', function () {

        $('.teamnameinput').html('<input type="text" id="textbox"><button class="submitteam">Save</button>');
        $('.submitteam').on('click', function () {
            var team_name = $('#textbox').val();
            var teamData = {'name': team_name};
            teamOfSix.push(team_name);

            name = JSON.stringify(teamData);
            $.ajax({
                url: '/new_team/',
                type: 'POST',
                dataType: 'json',
                data: name,
                success: function (data) {
                    save_team();
                    console.log(data)
                },
                error: function (data) {
                    console.log(data)
                }
            });
        });

        function save_team(){
            teamOfSix = JSON.stringify(teamOfSix);
            $.ajax({
                url: '/new_pokemon/',
                type: 'POST',
                dataType: 'json',
                data: teamOfSix,
                success: function (data) {
                    console.log(data)
                },
                error: function (data) {
                    console.log(data)
                }
            });
        }
    });
});

$('#getPokeInfoBtn').on('click', function() {
    $.ajax({
        url: '/pokemon_info/' + pokemonID + '/',
        type: 'GET',
        success: function(data) {
            $('.infoBlock').html(data);
        }
    });
});

$('#getPokeInfoBtn').on('click', function() {
    $.ajax({
        url: '/view_team/' + team_id + '/',
        type: 'GET',
        success: function(data) {
            $('.pokemonTeamInfo').html(data);
        }
    });
});