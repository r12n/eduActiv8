# -*- coding: utf-8 -*-

# this is a list of words used by the word builder and word maze games and possibly
# other games built in the future
# these words are mainly most commonly used words in English + some other words
# in each sub-list in the list di first number is a number of words in the sublist
# to aviod counting it every time list is selected
# the sublists are consisting of words with len() of 3 - 10
# I think the way of going about internationalization here would be to create a new list
# with words most commonly used in your language rather than translating this
# I am not sure if they are appriopriate for children, but if anyone is interested we can try to built something more suitable.

di = [[114, 'act', 'add', 'age', 'ago', 'air', 'all', 'and', 'any', 'are', 'art', 'bad', 'bed', 'big', 'bit', 'box',
       'boy', 'but', 'buy', 'can', 'car', 'cat', 'cry', 'cut', 'day', 'did', 'dog', 'dry', 'eat', 'end', 'far', 'few',
       'fig', 'fit', 'flu', 'fly', 'for', 'fun', 'gas', 'get', 'got', 'had', 'has', 'hat', 'her', 'him', 'his', 'hit',
       'hot', 'how', 'ice', 'its', 'job', 'key', 'law', 'lay', 'led', 'let', 'lie', 'lot', 'low', 'man', 'map', 'may',
       'men', 'new', 'nor', 'not', 'now', 'off', 'old', 'one', 'our', 'out', 'own', 'pay', 'per', 'pry', 'put', 'ran',
       'red', 'row', 'run', 'sat', 'saw', 'say', 'sea', 'see', 'set', 'she', 'sir', 'sit', 'six', 'ski', 'sky', 'son',
       'spy', 'sum', 'sun', 'ten', 'the', 'too', 'top', 'try', 'two', 'use', 'war', 'was', 'way', 'who', 'why', 'win',
       'yes', 'yet', 'you'],
      [381, 'able', 'also', 'area', 'arms', 'army', 'away', 'baby', 'back', 'ball', 'bank', 'base', 'bear', 'beat',
       'been', 'bell', 'best', 'bill', 'blab', 'blew', 'blip', 'blob', 'blot', 'blow', 'blue', 'boat', 'body', 'book',
       'born', 'both', 'bran', 'brat', 'bray', 'brew', 'brim', 'busy', 'came', 'care', 'case', 'city', 'clad', 'clam',
       'clan', 'clap', 'claw', 'clay', 'clip', 'clod', 'clog', 'club', 'clue', 'cold', 'come', 'cook', 'cool', 'copy',
       'corn', 'cost', 'cows', 'crab', 'crib', 'crop', 'crow', 'dark', 'deal', 'deep', 'does', 'done', 'door', 'down',
       'drab', 'drag', 'draw', 'drew', 'drip', 'drop', 'drum', 'each', 'ears', 'east', 'easy', 'edge', 'eggs', 'else',
       'even', 'ever', 'eyes', 'face', 'fact', 'fair', 'fall', 'farm', 'fast', 'fear', 'feel', 'feet', 'fell', 'felt',
       'find', 'fine', 'fire', 'fish', 'five', 'flag', 'flap', 'flat', 'flaw', 'flea', 'flew', 'flex', 'flip', 'flop',
       'flow', 'food', 'foot', 'four', 'free', 'frog', 'from', 'full', 'game', 'gave', 'girl', 'give', 'glad', 'glee',
       'glob', 'glow', 'glue', 'gold', 'gone', 'good', 'grab', 'gram', 'gray', 'grew', 'grid', 'grim', 'grin', 'grip',
       'grit', 'grow', 'grub', 'hair', 'halt', 'hand', 'hard', 'have', 'head', 'hear', 'heat', 'held', 'help', 'here',
       'high', 'hill', 'hold', 'hole', 'home', 'hope', 'huge', 'idea', 'into', 'iron', 'just', 'keep', 'kept', 'kind',
       'king', 'knew', 'know', 'lady', 'lake', 'land', 'last', 'lead', 'left', 'legs', 'less', 'life', 'like', 'line',
       'list', 'live', 'long', 'look', 'lost', 'loud', 'love', 'made', 'main', 'make', 'many', 'mark',
       'meat', 'meet', 'milk', 'mind', 'mine', 'miss', 'moon', 'more', 'most', 'move', 'much', 'must', 'name', 'near',
       'need', 'next', 'nose', 'note', 'noun', 'once', 'only', 'open', 'over', 'page', 'pair', 'park', 'part', 'past',
       'plan', 'play', 'plod', 'plot', 'plow', 'plug', 'plum', 'poem', 'pole', 'poor', 'pray', 'prod', 'prop', 'race',
       'rain', 'read', 'rest', 'rich', 'ride', 'ring', 'rise', 'road', 'rock', 'room', 'root', 'rope', 'rose', 'rule',
       'safe', 'said', 'sail', 'same', 'sand', 'save', 'scab', 'scan', 'scar', 'scat', 'seat', 'seen', 'sell', 'send',
       'sent', 'ship', 'shop', 'show', 'side', 'sign', 'sing', 'size', 'skid', 'skin', 'skip', 'skit', 'slab', 'slam',
       'slap', 'sled', 'slid', 'slim', 'slip', 'slit', 'slot', 'slow', 'slug', 'smog', 'snag', 'snap', 'snip', 'snob',
       'snow', 'snug', 'soft', 'soil', 'some', 'song', 'soon', 'span', 'spat', 'spin', 'spot', 'spur', 'star', 'stay',
       'stem', 'step', 'stew', 'stir', 'stop', 'such', 'sure', 'swam', 'swan', 'swap', 'swat', 'sway', 'swim', 'tail',
       'take', 'talk', 'tall', 'team', 'tell', 'test', 'than', 'that', 'them', 'then', 'they', 'thin', 'this', 'thus',
       'tied', 'time', 'tiny', 'told', 'tone', 'took', 'town', 'trap', 'tray', 'tree', 'trek', 'trim', 'trip', 'trot',
       'true', 'tube', 'turn', 'type', 'unit', 'upon', 'verb', 'very', 'view', 'wait', 'wall', 'want', 'warm', 'wash',
       'wear', 'week', 'well', 'went', 'were', 'west', 'what', 'when', 'wide', 'wife', 'wild', 'will', 'wind', 'wire',
       'wish', 'with', 'wood', 'work', 'yard', 'your'],
      [498, 'about', 'above', 'after', 'again', 'ahead', 'allow', 'alone', 'along', 'among', 'angle', 'apple', 'asked',
       'began', 'being', 'below', 'birds', 'black', 'blade', 'blame', 'blank', 'blast', 'blaze', 'bleat', 'bleed',
       'bleep', 'blend', 'bless', 'blind', 'blink', 'block', 'blood', 'bloom', 'bluff', 'blunt', 'blush', 'board',
       'bones', 'brace', 'braid', 'brain', 'brake', 'brand', 'brass', 'brave', 'brawl', 'bread', 'break', 'brick',
       'bride', 'bring', 'brisk', 'broad', 'broil', 'broke', 'brood', 'brook', 'broom', 'broth', 'brown', 'brush',
       'build', 'built', 'carry', 'catch', 'cause', 'cells', 'cents', 'chart', 'check', 'chief', 'child', 'clack',
       'claim', 'clamp', 'clang', 'clash', 'clasp', 'class', 'clean', 'clear', 'cleat', 'clerk', 'click', 'cliff',
       'climb', 'cling', 'clink', 'cloak', 'clock', 'clomp', 'close', 'cloth', 'cloud', 'clove', 'clown', 'cluck',
       'clump', 'coast', 'could', 'count', 'crack', 'craft', 'crane', 'crash', 'crawl', 'crazy', 'creek', 'creep',
       'cried', 'croak', 'crook', 'crops', 'cross', 'crowd', 'crown', 'crumb', 'crust', 'dance', 'draft', 'drain',
       'drake', 'drank', 'drape', 'dread', 'dream', 'dress', 'drift', 'drill', 'drink', 'drive', 'droop', 'drove',
       'early', 'earth', 'eight', 'enjoy', 'equal', 'every', 'field', 'fight', 'first', 'flake', 'flame', 'flare',
       'flash', 'fleck', 'fleet', 'flesh', 'flick', 'fling', 'flint', 'float', 'flock', 'flood', 'floor', 'floss',
       'flour', 'fluff', 'fluid', 'fluke', 'flunk', 'flush', 'flute', 'force', 'found', 'frail',
       'frame', 'frank', 'freak', 'fresh', 'frill', 'frizz', 'front', 'frost', 'fruit', 'glare', 'glass', 'gleam',
       'glide', 'gloat', 'globe', 'gloom', 'gloss', 'glove', 'grace', 'grade', 'graft', 'grain', 'grand', 'grant',
       'grape', 'graph', 'grasp', 'grass', 'grate', 'grave', 'gravy', 'graze', 'great', 'greed', 'green', 'greet',
       'grill', 'grime', 'grind', 'groan', 'groom', 'group', 'growl', 'grown', 'gruff', 'grump', 'guess', 'happy',
       'heard', 'heart', 'heavy', 'horse', 'hours', 'house', 'human', 'known', 'large', 'later', 'learn', 'least',
       'leave', 'level', 'light', 'major', 'march', 'match', 'maybe', 'means', 'metal', 'might', 'miles', 'money',
       'mouth', 'music', 'never', 'night', 'north', 'ocean', 'often', 'order', 'other', 'paint', 'paper', 'party',
       'piece', 'place', 'plaid', 'plain', 'plane', 'plank', 'plant', 'plate', 'plead', 'pleat', 'plink', 'plump',
       'point', 'power', 'press', 'price', 'pride', 'print', 'prize', 'probe', 'proof', 'proud', 'prove', 'prowl',
       'prune', 'quiet', 'quite', 'radio', 'ready', 'right', 'river', 'round', 'scald', 'scale', 'scalp', 'scamp',
       'scare', 'scarf', 'scold', 'scoop', 'scoot', 'scope', 'score', 'scour', 'scout', 'scram', 'scrap', 'screw',
       'scrub', 'scuba', 'scuff', 'seeds', 'sense', 'serve', 'seven', 'shall', 'shape', 'sharp', 'shoes', 'short',
       'shown', 'sight', 'since', 'skate', 'skill', 'skirt', 'skull', 'skunk', 'slack', 'slant', 'slate', 'sleek',
       'sleep', 'sleet', 'slept', 'slice', 'slick', 'slide', 'slime', 'sling', 'slope', 'slump', 'slush', 'smack',
       'small', 'smart', 'smash', 'smear', 'smell', 'smile', 'smock', 'smoke', 'snack', 'snail', 'snake', 'snare',
       'snarl', 'sneak', 'sniff', 'snoop', 'snore', 'snout', 'solve', 'sound', 'south', 'space', 'spare', 'spark',
       'speak', 'spear', 'speck', 'speed', 'spell', 'spend', 'spent', 'spike', 'spill', 'spine', 'spire', 'split',
       'spoil', 'spoke', 'spoon', 'sport', 'spout', 'spray', 'sprig', 'squat', 'squid', 'stack', 'staff', 'stage',
       'stain', 'stair', 'stake', 'stale', 'stalk', 'stall', 'stamp', 'stand', 'stare', 'stars', 'start', 'state',
       'steak', 'steal', 'steam', 'steel', 'steep', 'steer', 'stick', 'stiff', 'still', 'stilt', 'sting', 'stink',
       'stock', 'stone', 'stood', 'stool', 'stoop', 'store', 'storm', 'story', 'stove', 'strap', 'straw', 'stray',
       'strip', 'strum', 'study', 'style', 'sugar', 'swamp', 'swarm', 'sweat', 'sweep', 'sweet', 'swell', 'swept',
       'swift', 'swine', 'swing', 'swish', 'swoop', 'table', 'terms', 'their', 'there', 'these', 'thick', 'thing',
       'think', 'third', 'those', 'three', 'today', 'tools', 'total', 'touch', 'trace', 'track', 'trade', 'trail',
       'train', 'tramp', 'trash', 'tread', 'treat', 'trees', 'tribe', 'trick', 'troll', 'tromp', 'troop', 'trout',
       'truck', 'truly', 'trunk', 'trust', 'truth', 'uncle', 'under', 'until', 'value', 'visit', 'voice', 'vowel',
       'watch', 'water', 'waves', 'where', 'which', 'while', 'white', 'whole', 'whose', 'wings', 'woman', 'women',
       'words', 'world', 'would', 'write', 'wrong', 'wrote', 'years', 'young'],
      [242, 'across', 'action', 'afraid', 'agreed', 'almost', 'always', 'amount', 'answer', 'appear', 'around',
       'became', 'become', 'before', 'behind', 'belong', 'beside', 'better', 'bleach', 'blonde', 'blouse', 'bottom',
       'bought', 'braise', 'branch', 'breath', 'breeze', 'bridge', 'bright', 'broken', 'bronco', 'bronze', 'browse',
       'bruise', 'called', 'cannot', 'cattle', 'caught', 'centre', 'chance', 'change', 'choose', 'church', 'circle',
       'closet', 'clutch', 'colour', 'column', 'common', 'corner', 'cotton', 'course', 'cradle', 'crayon', 'create',
       'crunch', 'desert', 'design', 'direct', 'doctor', 'dragon', 'during', 'effect', 'either', 'energy', 'engine',
       'enough', 'entire', 'except', 'expect', 'family', 'famous', 'father', 'figure', 'filled', 'flight', 'flower',
       'forest', 'freeze', 'friend', 'fright', 'fringe', 'frozen', 'garden', 'glance', 'glitch', 'grapes', 'grease',
       'grouch', 'ground', 'grudge', 'inches', 'inside', 'island', 'itself', 'joined', 'jumped', 'killed', 'length',
       'lifted', 'listen', 'little', 'matter', 'melody', 'method', 'middle', 'modern', 'moment', 'months', 'mother',
       'nation', 'notice', 'number', 'object', 'office', 'oxygen', 'passed', 'people', 'period', 'person', 'phrase',
       'picked', 'plains', 'planet', 'plants', 'player', 'please', 'pledge', 'plenty', 'plural', 'pounds', 'praise',
       'prance', 'prayer', 'pretty', 'priest', 'prince', 'prison', 'pulled', 'pushed', 'raised', 'rather', 'really',
       'reason', 'record', 'region', 'remain', 'report', 'result', 'return', 'rhythm', 'rolled', 'scarce', 'school',
       'scorch', 'scrape', 'scrawl', 'scream', 'screen', 'script', 'scroll', 'second', 'seemed', 'should', 'silent',
       'simple', 'single', 'sister', 'sketch', 'sleepy', 'sleeve', 'slight', 'slowly', 'smiled', 'smooth', 'smudge',
       'snatch', 'sneeze', 'speech', 'spirit', 'splash', 'splint', 'sponge', 'sprain', 'sprang', 'sprawl', 'spread',
       'spring', 'sprint', 'sprout', 'spruce', 'square', 'squash', 'squeak', 'squeal', 'squint', 'squirm', 'squirt',
       'squish', 'stable', 'staple', 'starch', 'starve', 'statue', 'steady', 'stereo', 'sticky', 'stingy', 'stitch',
       'strain', 'strand', 'streak', 'stream', 'street', 'strict', 'stride', 'strike', 'string', 'stripe', 'stroke',
       'stroll', 'strong', 'struck', 'suffix', 'summer', 'supply', 'swatch', 'swerve', 'switch', 'system', 'though',
       'toward', 'travel', 'trough', 'valley', 'walked', 'weight', 'wheels', 'window', 'winter', 'within', 'wonder',
       'yellow'],
      [142, 'against', 'already', 'animals', 'another', 'arrived', 'because', 'believe', 'between', 'blanket',
       'blossom', 'brother', 'brought', 'burning', 'capital', 'captain', 'century', 'certain', 'climate', 'climbed',
       'clothes', 'company', 'compare', 'contain', 'control', 'correct', 'country', 'covered', 'cricket', 'current',
       'decided', 'decimal', 'details', 'distant', 'divided', 'dollars', 'drawing', 'entered', 'evening', 'exactly',
       'example', 'explain', 'express', 'factors', 'farmers', 'feeling', 'finally', 'fingers', 'flowers', 'forward',
       'freight', 'friends', 'general', 'gravity', 'himself', 'history', 'however', 'hundred', 'hunting', 'include',
       'insects', 'instead', 'laughed', 'letters', 'located', 'machine', 'measure', 'members', 'million', 'minutes',
       'morning', 'natural', 'nothing', 'numeral', 'observe', 'outside', 'pattern', 'perhaps', 'picture', 'planets',
       'prepare', 'present', 'pretzel', 'printed', 'problem', 'process', 'produce', 'product', 'program', 'project',
       'promise', 'pronoun', 'protect', 'provide', 'quickly', 'reached', 'scallop', 'science', 'scooter', 'scraper',
       'scratch', 'screech', 'section', 'settled', 'several', 'shouted', 'similar', 'skillet', 'slipper', 'snuggle',
       'someone', 'special', 'squeeze', 'stadium', 'stapler', 'started', 'station', 'stirrup', 'stomach', 'strange',
       'stretch', 'subject', 'suppose', 'surface', 'swallow', 'sweater', 'sweeten', 'swollen', 'symbols', 'teacher',
       'thought', 'through', 'trouble', 'trumpet', 'usually', 'various', 'village', 'weather', 'western', 'whether',
       'without', 'workers', 'written'],
      [76, 'actually', 'addition', 'although', 'anything', 'blizzard', 'branches', 'building', 'business', 'children',
       'clothing', 'complete', 'compound', 'consider', 'describe', 'division', 'electric', 'elements', 'equation',
       'everyone', 'exciting', 'exercise', 'finished', 'fraction', 'freckles', 'happened', 'increase', 'indicate',
       'industry', 'interest', 'language', 'material', 'movement', 'northern', 'opposite', 'pleasant', 'position',
       'possible', 'practice', 'practise', 'precious', 'prepared', 'princess', 'prisoner', 'probably', 'products',
       'property', 'received', 'remember', 'repeated', 'scallion', 'scramble', 'scribble', 'sentence', 'separate',
       'shoulder', 'soldiers', 'solution', 'southern', 'splendid', 'splinter', 'sprinkle', 'squirrel', 'starfish',
       'stocking', 'straight', 'strainer', 'stranger', 'strength', 'stronger', 'struggle', 'students', 'suddenly',
       'surprise', 'together', 'triangle', 'yourself'],
      [36, 'adjective', 'beautiful', 'beginning', 'carefully', 'consonant', 'continued', 'determine', 'developed',
       'different', 'difficult', 'direction', 'factories', 'following', 'groceries', 'important', 'molecules',
       'mountains', 'necessary', 'paragraph', 'president', 'principal', 'professor', 'pronounce', 'propeller',
       'questions', 'represent', 'something', 'sometimes', 'sprinkler', 'statement', 'stretched', 'stretcher',
       'suggested', 'syllables', 'thousands', 'underline'],
      [18, 'blackboard', 'conditions', 'dictionary', 'difference', 'discovered', 'especially', 'everything',
       'experience', 'experiment', 'flashlight', 'government', 'particular', 'scientists', 'stationary', 'strawberry',
       'substances', 'themselves', 'understand']]
