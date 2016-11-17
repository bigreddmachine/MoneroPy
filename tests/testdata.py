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
addr_vers = '12'
valid_addr_pubsks = [
    '426a2b555065c79b8d6293c5dd18c25a25bae1a8b8c67ceac7484133e6798579',
    '975e989ae39b7b9445ac7384edb7a598efe3fbfab6c0bd72c5372fadd86071e9',
    'b9e8cd1f42a48c55166f75ead8293e0ad1c420f566b9c85562572936207557dd',
    'c09d10f3c5f580ddd0765063d9246007f45ef025a76c7d117fe4e811fa78f395',
    'bd785822c5e8330e30cc7e6e7abd3d11579da04e4131d091255172583059aea5'
]
valid_addr_pubvks = [
    'bba3444bd48d5d9fcffa64d805e3977b07e2d420a2212df3d612a5dbcc676538',
    '5096d3b5eedd396ea5c521456640fb27ebb5a222269eac49e1ddac7134735ea0',
    '08613f96d197024ea651e8f226feb03b71aa82f487cb6eff518a30a3b6a2514f',
    '9c66f7487c1bef43c64ee0ace763116456666a389eea3b693cd7670c3515a0c0',
    '8501a7d7657332995b54357cc02c972c5cf5b2d1804d4d273c6f214854c9cf7e'
]


# These can be tested against valid_addrs for base588 encode/decode
decoded_addrs = [
    '12426a2b555065c79b8d6293c5dd18c25a25bae1a8b8c67ceac7484133e6798579bba3444bd48d5d9fcffa64d805e3977b07e2d420a2212df3d612a5dbcc67653844ded707',
    '12975e989ae39b7b9445ac7384edb7a598efe3fbfab6c0bd72c5372fadd86071e95096d3b5eedd396ea5c521456640fb27ebb5a222269eac49e1ddac7134735ea0efb2b899',
    '12b9e8cd1f42a48c55166f75ead8293e0ad1c420f566b9c85562572936207557dd08613f96d197024ea651e8f226feb03b71aa82f487cb6eff518a30a3b6a2514f0eb176af',
    '12c09d10f3c5f580ddd0765063d9246007f45ef025a76c7d117fe4e811fa78f3959c66f7487c1bef43c64ee0ace763116456666a389eea3b693cd7670c3515a0c043794fbf',
    '12bd785822c5e8330e30cc7e6e7abd3d11579da04e4131d091255172583059aea58501a7d7657332995b54357cc02c972c5cf5b2d1804d4d273c6f214854c9cf7edd34d73c'
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
extra_hex = [
    '01e0a4a7a6acf619da6ce1e2570c0c3439f5f809f101360859268648b4f8ec654e',
    '012f72986164c41ae40c838d27b6923297552cea015bf73f9580be84c9cc3743b2',
    '022100c80ab4d153c7fec09fd502096e41fbe421764616a3fc62483928c5a77b6d7ece015696990c2d33ef90235216684f7a44c4c2ff73460fdf01f1353003d6bcdf3774',
    '0150141de1b549bf59d949cf03723b04a51a93203e2ae6211e2f173f6ab44ee1b90221003f829f11a7768559de4e0072baa81cfd861d810e23b81b2dd949258956458fb7de204edba8bb1837d21a611848a62b6a8a6fdf9a7b08ba21679fac6a117db56e2b35',
    '0111e8f0ae2ff804561e718ee132a9a8f17b3b50abd23774cf023c93916e2da49702112c840e01000000000000000000000000000321002ad3ef991096aff1c59a234920c5531baf9e2efba420b293e1a40b9796b652bd'
]
extra_bin = [
    [1, 224, 164, 167, 166, 172, 246, 25, 218, 108, 225, 226, 87, 12, 12, 52, 57, 245, 248, 9, 241, 1, 54, 8, 89, 38, 134, 72, 180, 248, 236, 101, 78],
    [1, 47, 114, 152, 97, 100, 196, 26, 228, 12, 131, 141, 39, 182, 146, 50, 151, 85, 44, 234, 1, 91, 247, 63, 149, 128, 190, 132, 201, 204, 55, 67, 178],
    [2, 33, 0, 200, 10, 180, 209, 83, 199, 254, 192, 159, 213, 2, 9, 110, 65, 251, 228, 33, 118, 70, 22, 163, 252, 98, 72, 57, 40, 197, 167, 123, 109, 126, 206, 1, 86, 150, 153, 12, 45, 51, 239, 144, 35, 82, 22, 104, 79, 122, 68, 196, 194, 255, 115, 70, 15, 223, 1, 241, 53, 48, 3, 214, 188, 223, 55, 116],
    [1, 80, 20, 29, 225, 181, 73, 191, 89, 217, 73, 207, 3, 114, 59, 4, 165, 26, 147, 32, 62, 42, 230, 33, 30, 47, 23, 63, 106, 180, 78, 225, 185, 2, 33, 0, 63, 130, 159, 17, 167, 118, 133, 89, 222, 78, 0, 114, 186, 168, 28, 253, 134, 29, 129, 14, 35, 184, 27, 45, 217, 73, 37, 137, 86, 69, 143, 183, 222, 32, 78, 219, 168, 187, 24, 55, 210, 26, 97, 24, 72, 166, 43, 106, 138, 111, 223, 154, 123, 8, 186, 33, 103, 159, 172, 106, 17, 125, 181, 110, 43, 53],
    [1, 17, 232, 240, 174, 47, 248, 4, 86, 30, 113, 142, 225, 50, 169, 168, 241, 123, 59, 80, 171, 210, 55, 116, 207, 2, 60, 147, 145, 110, 45, 164, 151, 2, 17, 44, 132, 14, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 33, 0, 42, 211, 239, 153, 16, 150, 175, 241, 197, 154, 35, 73, 32, 197, 83, 27, 175, 158, 46, 251, 164, 32, 178, 147, 225, 164, 11, 151, 150, 182, 82, 189]
]
extra_pub = [
    'e0a4a7a6acf619da6ce1e2570c0c3439f5f809f101360859268648b4f8ec654e',
    '2f72986164c41ae40c838d27b6923297552cea015bf73f9580be84c9cc3743b2',
    '5696990c2d33ef90235216684f7a44c4c2ff73460fdf01f1353003d6bcdf3774',
    '50141de1b549bf59d949cf03723b04a51a93203e2ae6211e2f173f6ab44ee1b9',
    '11e8f0ae2ff804561e718ee132a9a8f17b3b50abd23774cf023c93916e2da497'
]
extra_payid = [
    '',
    '',
    'c80ab4d153c7fec09fd502096e41fbe421764616a3fc62483928c5a77b6d7ece',
    '3f829f11a7768559de4e0072baa81cfd861d810e23b81b2dd949258956458fb7',
    ''
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
