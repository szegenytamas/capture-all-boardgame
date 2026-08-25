from pygame.math import Vector2

CELL_SIZE = 42
BOARD_WIDTH = 26
BOARD_HEIGHT = 19
ANIMALS_TO_CATCH = 20


STARTING_POINTS = [Vector2(8, 0), Vector2(
    0, 3), Vector2(0, 14), Vector2(7, 18), Vector2(17, 18), Vector2(25, 15), Vector2(25, 4), Vector2(18, 0)]
FORBIDDEN_BLOCKS = [Vector2(2, 4), Vector2(
    3, 11), Vector2(2, 15), Vector2(8, 12), Vector2(9, 2), Vector2(8, 6), Vector2(9, 17), Vector2(11, 11), Vector2(13, 7), Vector2(17, 5), Vector2(20, 1), Vector2(24, 6), Vector2(23, 14), Vector2(18, 12), Vector2(16, 16), Vector2(17, 9)]
OFFSETS = [
    Vector2(-1, -2), Vector2(1, -2), Vector2(2, -1), Vector2(2, 1),
    Vector2(1, 2), Vector2(-1, 2), Vector2(-2, 1), Vector2(-2, -1)
]


P_COLORS = (('white', (255, 255, 255)), ('pink', (249, 3, 255)), ('blue', (
    0, 162, 232)), ('red', (136, 0, 21)), ('orange', (255, 127, 39)), ('green', (34, 177, 76)))
A_COLORS = {'green': (2, 158, 4), 'skin': (255, 187, 115),
            'orange': (250, 141, 0), 'blue': (77, 138, 255), 'pink': (255, 77, 190), 'brown': (145, 101, 81), 'gray': (130, 130, 130), 'red': (255, 0, 0)}

ANIMAL_PICTURES = {'albatross': 'graphics/animals/albatross.png',
                   'sealion': 'graphics/animals/sealion.png',
                   'penguin': 'graphics/animals/penguin.png',
                   'reindeer': 'graphics/animals/reindeer.png',
                   'wolf': 'graphics/animals/wolf.png',
                   'moose': 'graphics/animals/moose.png',
                   'otter': 'graphics/animals/sea-otter.png',
                   'lynx': 'graphics/animals/lynx.png',
                   'arcticfox': 'graphics/animals/arcticfox.png',
                   'sable': 'graphics/animals/sable.png',
                   'polarbear': 'graphics/animals/polarbear.png',
                   'boar': 'graphics/animals/wild-boar.png',
                   'grizzly': 'graphics/animals/grizzly.png',
                   'walrus': 'graphics/animals/walrus.png',
                   'damdeer': 'graphics/animals/damdeer.png',
                   'brownbear': 'graphics/animals/brownbear.png',
                   'eagle': 'graphics/animals/eagle.png',
                   'goat': 'graphics/animals/goat.png',
                   'roedeer': 'graphics/animals/roedeer.png',
                   'heron': 'graphics/animals/heron.png',
                   'yak': 'graphics/animals/yak.png',
                   'bison': 'graphics/animals/bison.png',
                   'hare': 'graphics/animals/hare.png',
                   'pheasant': 'graphics/animals/pheasant.png',
                   'caucasiangoat': 'graphics/animals/caucasiangoat.png',
                   'mouflon': 'graphics/animals/mouflon.png',
                   'fox': 'graphics/animals/fox.png',
                   'marabou': 'graphics/animals/marabou.png',
                   'jackal': 'graphics/animals/jackal.png',
                   'crane': 'graphics/animals/crane.png',
                   'crane_2': 'graphics/animals/crane_2.png',
                   'armadillo': 'graphics/animals/armadillo.png',
                   'owl': 'graphics/animals/owl.png',
                   'reddeer': 'graphics/animals/reddeer.png',
                   'hyena': 'graphics/animals/hyena.png',
                   'hippo': 'graphics/animals/hippo.png',
                   'bezoargoat': 'graphics/animals/bezoargoat.png',
                   'tapir': 'graphics/animals/tapir.png',
                   'wild-boar': 'graphics/animals/wild-boar.png',
                   'tiger': 'graphics/animals/tiger.png',
                   'lion': 'graphics/animals/lion.png',
                   'skunk': 'graphics/animals/skunk.png',
                   'howler-monkey': 'graphics/animals/howler-monkey.png',
                   'gorilla': 'graphics/animals/gorilla.png',
                   'antelope': 'graphics/animals/antelope.png',
                   'pelican': 'graphics/animals/pelican.png',
                   'indianrhino': 'graphics/animals/indianrhino.png',
                   'whiterhino': 'graphics/animals/whiterhino.png',
                   'flamingo': 'graphics/animals/flamingo.png',
                   'cobra': 'graphics/animals/cobra.png',
                   'polecat': 'graphics/animals/polecat.png',
                   'leopard': 'graphics/animals/leopard.png',
                   'elephant': 'graphics/animals/elephant.png',
                   'crocodile': 'graphics/animals/crocodile.png',
                   'pangolin': 'graphics/animals/pangolin.png',
                   'sloth': 'graphics/animals/sloth.png',
                   'okapi': 'graphics/animals/okapi.png',
                   'kudu': 'graphics/animals/kudu.png',
                   'red-panda': 'graphics/animals/red-panda.png',
                   'chimpanzee': 'graphics/animals/chimpanzee.png',
                   'gnu': 'graphics/animals/gnu.png',
                   'racoon': 'graphics/animals/racoon.png',
                   'bongo': 'graphics/animals/bongo.png',
                   'zebra': 'graphics/animals/zebra.png',
                   'giraffe': 'graphics/animals/giraffe.png',
                   'beizaantelope': 'graphics/animals/beizaantelope.png',
                   'warthog': 'graphics/animals/warthog.png',
                   'blackbear': 'graphics/animals/blackbear.png',
                   'gazelle': 'graphics/animals/gazelle.png',
                   'badger': 'graphics/animals/badger.png',
                   'condor': 'graphics/animals/condor.png',
                   'nyala': 'graphics/animals/nyala.png',
                   'anteater': 'graphics/animals/anteater.png',
                   'ostrich': 'graphics/animals/ostrich.png',
                   'buffalo': 'graphics/animals/buffalo.png',
                   'blackpanther': 'graphics/animals/blackpanther.png',
                   'javorantelope': 'graphics/animals/javorantelope.png',
                   'aardvark': 'graphics/animals/aardvark.png',
                   'kangaroo': 'graphics/animals/kangaroo.png',
                   'turtle': 'graphics/animals/turtle.png'
                   }
