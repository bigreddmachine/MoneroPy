# These seeds, sks, vks, and addrs are all valid and derived from one another:
valid_seeds = [
    ['zebra','oasis','oncoming','wobbly','yawning','tiers','reef','friendly','maze','shyness','unknown','eavesdrop','zapped','lumber','often','spiders','twang','afloat','elite','vein','auctions','ingested','demonstrate','diplomat','vein'],
    ['urgent','loaded','linen','uncle','occur','jockey','cynical','himself','keyboard','lectures','tobacco','racetrack','empty','diode','erosion','merger','upright','wagtail','eternal','getting','dangerous','dazed','speedy','stacking','racetrack'],
    ['womanly','afield','obedient','quote','square','apex','sphere','poetry','wives','agony','axes','bowling','narrate','coal','aided','vivid','sowed','ignore','sensible','randomly','muddy','oxygen','onto','ouch','wives'],
    ['owed','cement','roomy','ought','fugitive','wrong','island','avidly','catch','zippers','layout','sovereign','suitcase','rogue','fewest','doorway','unlikely','feel','lion','bugs','second','tomorrow','diplomat','edited','ought'],
    ['wrong','otter','jukebox','twofold','reorder','doing','idled','dosage','jigsaw','symptoms','tomorrow','umpire','justice','python','butter','opus','aisle','soda','punch','tuition','slower','emerge','island','joining','punch']
]
valid_sks = [
    '641731042d78e2ddef3340371e51bf55c6ec8f1757d4d6222976d324e230cd02',
    'e72462ff644844d902824e1597d5e7d5768ce80fe84e9e0a27c1d9d801258401',
    'b112829329fcbc3ecc0c754e353e180afc2865dff2d0699aeae0eed938694e03',
    '44bea1954de9e0abaff67d10a5dda652bf530590ab786363e478a0a196ca5909',
    '235c87d42f9dd47ef455da3b3d41c806763e2f71c18a1ac4aac478e8e379b305'
]
valid_vks = [
    '158b0dec091eeb4476422d26830c75794ae9a003015a523fdac75ed78cd3e309',
    '357f5f7e8b6eab22c4e7fde17ca77d026fa2b9155c4d51239bdbe02a5ddea90c',
    '729dc201f1370795789006c1caec15bad7022aaf63a2d8e1087bb069298baa09',
    '7f0c51be394bf8ab629f952b77dbbd90b1f7df17cb228024173460cdf7489401',
    '57e9d09d40114bd69a81feef0a67eedf097e500ab018de86d6f63eb2e7446503'
]
valid_addrs = [
    '4495qPNxDGAT241zya1WdwG5YU6RQ6s7ZgGeQryFtooAMMxoqx2N2oNTjP5NTqDf9GMaZ52iS2Q6xhnWyW16cdi47MCsVRg',
    '47Mov77LGqgRoRh6K6XVheSagWVRS7jkQLCR9jPQxTa8g2SrnwbWuMzKWRLyyBFsxn7gHJv15987MDMkYXCXGGvhKA7Qsx4',
    '48fj5P3zky9FETVG144GWh2oxnEdBc45VFHLKgKQfZ7UdyJ5M7mDFxuEA12eBuD55RAwgX2jzFYfwjhukHavcLHW9vKn1VG',
    '48vTj54ZtU7e6sqwcJY9uq2LApd3Zi6H23vmYFc3wMteS2QzJwi2Z1xCLVwMac55h2HnQAiYwZTceJbwMZJRrm3uNh76Hci',
    '48oYzqzeGqY3Nfg6LG8HwS3uF1Y3vV2gfRH6ZMcnhhEmUgkL2mPSjtuSekenrYGkbp8RNvAvrtq3r7Ze4iPoBH3kFK9vbgP'
]

# These seeds have the wrong checksum. For test_mnemonic.py:
invalid_seeds = [
    ['zebra','oasis','oncoming','wobbly','yawning','tiers','reef','friendly','maze','shyness','unknown','eavesdrop','zapped','lumber','often','spiders','twang','afloat','elite','vein','auctions','ingested','demonstrate','diplomat','diplomat'],
    ['urgent','loaded','linen','uncle','occur','jockey','cynical','himself','keyboard','lectures','tobacco','racetrack','empty','diode','erosion','merger','upright','wagtail','eternal','getting','dangerous','dazed','speedy','stacking','dangerous'],
    ['womanly','afield','obedient','quote','square','apex','sphere','poetry','wives','agony','axes','bowling','narrate','coal','aided','vivid','sowed','ignore','sensible','randomly','muddy','oxygen','onto','ouch','oxygen'],
    ['owed','cement','roomy','ought','fugitive','wrong','island','avidly','catch','zippers','layout','sovereign','suitcase','rogue','fewest','doorway','unlikely','feel','lion','bugs','second','tomorrow','diplomat','edited','bugs'],
    ['wrong','otter','jukebox','twofold','reorder','doing','idled','dosage','jigsaw','symptoms','tomorrow','umpire','justice','python','butter','opus','aisle','soda','punch','tuition','slower','emerge','island','joining','tuition']
]

# For test_utils.py:
hexes = [
    '641731042d78e2ddef3340371e51bf55c6ec8f1757d4d6222976d324e230cd02',
    'e72462ff644844d902824e1597d5e7d5768ce80fe84e9e0a27c1d9d801258401',
    'b112829329fcbc3ecc0c754e353e180afc2865dff2d0699aeae0eed938694e03',
    '44bea1954de9e0abaff67d10a5dda652bf530590ab786363e478a0a196ca5909',
    '235c87d42f9dd47ef455da3b3d41c806763e2f71c18a1ac4aac478e8e379b305'
]
ints = [
    1267166726096927029789014970606765322553773056507777453263144086171181717348,
    685792075545825044641993933091589991867261783922969064258564262430660240615,
    1495478832876975752448424395286770096003750226651159965005740393562225382065,
    4229463239790018874285924388021495332866381457501964753336570234542254833220,
    2578671123209650673872865557522209656331423257703416053928268301946856102947
]

# For test_cryptonote.py
hashed_valid_sks = [
    '317a934746c3c765829cc8c9f2c2e8734be9a003015a523fdac75ed78cd3e3c9',
    'fcfa4095da97e22a47bee4ca18951a416fa2b9155c4d51239bdbe02a5ddea93c',
    'ed687b8ca9ed87fd54dacb35e1c12e4cd8022aaf63a2d8e1087bb069298baa79',
    'fad70949f20079143fe95aa08db0d622b2f7df17cb228024173460cdf7489471',
    'e5e093cbde63b9e6a02eccc14242285d0a7e500ab018de86d6f63eb2e7446563'
]

reduced_hashed_valid_sks = [
    '158b0dec091eeb4476422d26830c75794ae9a003015a523fdac75ed78cd3e309',
    '357f5f7e8b6eab22c4e7fde17ca77d026fa2b9155c4d51239bdbe02a5ddea90c',
    '729dc201f1370795789006c1caec15bad7022aaf63a2d8e1087bb069298baa09',
    '7f0c51be394bf8ab629f952b77dbbd90b1f7df17cb228024173460cdf7489401',
    '57e9d09d40114bd69a81feef0a67eedf097e500ab018de86d6f63eb2e7446503'
]

public_from_valid_sks = [
    '426a2b555065c79b8d6293c5dd18c25a25bae1a8b8c67ceac7484133e6798579',
    '975e989ae39b7b9445ac7384edb7a598efe3fbfab6c0bd72c5372fadd86071e9',
    'b9e8cd1f42a48c55166f75ead8293e0ad1c420f566b9c85562572936207557dd',
    'c09d10f3c5f580ddd0765063d9246007f45ef025a76c7d117fe4e811fa78f395',
    'bd785822c5e8330e30cc7e6e7abd3d11579da04e4131d091255172583059aea5'
]
