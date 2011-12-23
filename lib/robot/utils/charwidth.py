#  Copyright 2008-2011 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


"""A module to handle different character widths on the console.

Some East Asian characters have width of two on console, and combining
characters themselves take no extra space.

See issue 604 [1] for more details. It also contains `generate_wild_chars.py`
script that was originally used to create the East Asian wild character map.
Big thanks for xieyanbo for the script and the original patch.

Note that Python's `unicodedata` module is not used here because importing
it takes several seconds on Jython.

[1] http://code.google.com/p/robotframework/issues/detail?id=604
"""

def get_char_width(char):
    char = ord(char)
    if _char_in_map(char, _COMBINING_CHARS):
        return 0
    if _char_in_map(char, _EAST_ASIAN_WILD_CHARS):
        return 2
    return 1

def _char_in_map(char, map):
    for begin, end in map:
        if char < begin:
            break
        if begin <= char <= end:
            return True
    return False


_COMBINING_CHARS = [(768,879)]

_EAST_ASIAN_WILD_CHARS = [
        (888, 889), (896, 899), (909, 909), (1316, 1328), (1368, 1368),
        (1416, 1416), (1420, 1424), (1481, 1487), (1516, 1519),
        (1526, 1535), (1541, 1541), (1565, 1565), (1631, 1631),
        (1867, 1868), (1971, 1983), (2044, 2304), (2363, 2363),
        (2383, 2383), (2390, 2391), (2420, 2426), (2436, 2436),
        (2446, 2446), (2450, 2450), (2481, 2481), (2484, 2485),
        (2491, 2491), (2502, 2502), (2506, 2506), (2512, 2518),
        (2521, 2523), (2532, 2533), (2556, 2560), (2571, 2574),
        (2578, 2578), (2609, 2609), (2615, 2615), (2619, 2619),
        (2627, 2630), (2634, 2634), (2639, 2640), (2643, 2648),
        (2655, 2661), (2679, 2688), (2702, 2702), (2729, 2729),
        (2740, 2740), (2747, 2747), (2762, 2762), (2767, 2767),
        (2770, 2783), (2789, 2789), (2802, 2816), (2829, 2830),
        (2834, 2834), (2865, 2865), (2874, 2875), (2886, 2886),
        (2890, 2890), (2895, 2901), (2905, 2907), (2916, 2917),
        (2931, 2945), (2955, 2957), (2966, 2968), (2973, 2973),
        (2977, 2978), (2982, 2983), (2988, 2989), (3003, 3005),
        (3012, 3013), (3022, 3023), (3026, 3030), (3033, 3045),
        (3068, 3072), (3085, 3085), (3113, 3113), (3130, 3132),
        (3145, 3145), (3151, 3156), (3162, 3167), (3173, 3173),
        (3185, 3191), (3201, 3201), (3213, 3213), (3241, 3241),
        (3258, 3259), (3273, 3273), (3279, 3284), (3288, 3293),
        (3300, 3301), (3315, 3329), (3341, 3341), (3369, 3369),
        (3387, 3388), (3401, 3401), (3407, 3414), (3417, 3423),
        (3429, 3429), (3447, 3448), (3457, 3457), (3479, 3481),
        (3516, 3516), (3519, 3519), (3528, 3529), (3532, 3534),
        (3543, 3543), (3553, 3569), (3574, 3584), (3644, 3646),
        (3677, 3712), (3717, 3718), (3723, 3724), (3727, 3731),
        (3744, 3744), (3750, 3750), (3753, 3753), (3770, 3770),
        (3775, 3775), (3783, 3783), (3791, 3791), (3803, 3803),
        (3807, 3839), (3949, 3952), (3981, 3983), (4029, 4029),
        (4053, 4095), (4251, 4253), (4295, 4303), (4350, 4447),
        (4516, 4519), (4603, 4607), (4686, 4687), (4697, 4697),
        (4703, 4703), (4750, 4751), (4790, 4791), (4801, 4801),
        (4807, 4807), (4881, 4881), (4887, 4887), (4956, 4958),
        (4990, 4991), (5019, 5023), (5110, 5120), (5752, 5759),
        (5790, 5791), (5874, 5887), (5909, 5919), (5944, 5951),
        (5973, 5983), (6001, 6001), (6005, 6015), (6111, 6111),
        (6123, 6127), (6139, 6143), (6170, 6175), (6265, 6271),
        (6316, 6399), (6430, 6431), (6445, 6447), (6461, 6463),
        (6466, 6467), (6511, 6511), (6518, 6527), (6571, 6575),
        (6603, 6607), (6619, 6621), (6685, 6685), (6689, 6911),
        (6989, 6991), (7038, 7039), (7084, 7085), (7099, 7167),
        (7225, 7226), (7243, 7244), (7297, 7423), (7656, 7677),
        (7959, 7959), (7967, 7967), (8007, 8007), (8015, 8015),
        (8026, 8026), (8030, 8030), (8063, 8063), (8133, 8133),
        (8149, 8149), (8176, 8177), (8191, 8191), (8294, 8297),
        (8307, 8307), (8341, 8351), (8375, 8399), (8434, 8447),
        (8529, 8530), (8586, 8591), (9002, 9002), (9193, 9215),
        (9256, 9279), (9292, 9311), (9887, 9887), (9918, 9919),
        (9925, 9984), (9994, 9995), (10060, 10060), (10067, 10069),
        (10079, 10080), (10134, 10135), (10175, 10175), (10189, 10191),
        (11086, 11087), (11094, 11263), (11359, 11359), (11390, 11391),
        (11500, 11512), (11559, 11567), (11623, 11630), (11633, 11647),
        (11672, 11679), (11695, 11695), (11711, 11711), (11727, 11727),
        (11743, 11743), (11826, 12350), (12353, 19903), (19969, 42239),
        (42541, 42559), (42593, 42593), (42613, 42619), (42649, 42751),
        (42894, 43002), (43053, 43071), (43129, 43135), (43206, 43213),
        (43227, 43263), (43349, 43358), (43361, 43519), (43576, 43583),
        (43599, 43599), (43611, 43611), (43617, 55295), (63745, 64255),
        (64264, 64274), (64281, 64284), (64317, 64317), (64322, 64322),
        (64434, 64466), (64833, 64847), (64913, 64913), (64969, 65007),
        (65023, 65023), (65041, 65055), (65064, 65135), (65277, 65278),
        (65281, 65376), (65472, 65473), (65481, 65481), (65489, 65489),
        (65497, 65497), (65502, 65511), (65520, 65528), (65535, 65535),
        ]