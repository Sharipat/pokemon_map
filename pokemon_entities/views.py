import folium
from django.http import HttpResponseNotFound
from pokemon_entities.models import Pokemon, PokemonEntity
from django.shortcuts import render

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, level, health, strength, defence,
                stamina, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        popup=folium.Popup("""
        Уровень: {}
        Здоровье: {}
        Атака: {}
        Защита: {}
        Выносливость: {}""".format(level, health, strength, defence, stamina)),
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.select_related().all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        absolute_uri = request.build_absolute_uri(
            pokemon_entity.pokemon.image.url)
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            pokemon_entity.level,
            pokemon_entity.health,
            pokemon_entity.strength,
            pokemon_entity.defence,
            pokemon_entity.stamina,
            absolute_uri)

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url
            if pokemon.image else DEFAULT_IMAGE_URL,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):

    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound(
            '<h1>Такой покемон не найден</h1>')

    pokemon_entities = pokemon.entities.filter(pokemon=pokemon)
    all_elements = pokemon.element_type.all()
    folium_map = folium.Map(
        location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        absolute_uri = request.build_absolute_uri(
            pokemon_entity.pokemon.image.url)
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            pokemon_entity.level,
            pokemon_entity.health,
            pokemon_entity.strength,
            pokemon_entity.defence,
            pokemon_entity.stamina,
            absolute_uri)

    pokemon_elements = []
    strong_against = []
    for element in all_elements:
        pokemon_elements.append({
            'img': element.image.url,
            'title': element.title})
        for strong in element.strong_against.all():
            strong_against.append(strong.title)

    pokemon_info = {
        'pokemon_id': pokemon.id,
        'img_url': pokemon.image.url,
        'title_ru': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'element_type': pokemon_elements
    }

    pokemon_previous_evolution = pokemon.previous_evolution

    if pokemon_previous_evolution:
        pokemon_info['previous_evolution'] = {
            'title_ru': pokemon_previous_evolution.title,
            'pokemon_id': pokemon_previous_evolution.id,
            'img_url': pokemon_previous_evolution.image.url
        }

    pokemon_next_evolution = pokemon.next_evolution.first()
    if pokemon_next_evolution:
        pokemon_info['next_evolution'] = {
            'title_ru': pokemon_next_evolution.title,
            'pokemon_id': pokemon_next_evolution.id,
            'img_url': pokemon_next_evolution.image.url,
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_info
    })
