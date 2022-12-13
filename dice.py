from itertools import product
from json import dumps
import re


faces = '万火水冰雷风草岩'
re_d_ele = re.compile(r'\d+.')


def work(roll=8, target='3雷3草', keep='', rerolls=1):
    print(f"需要{target}，{f'已保留{keep}，' if keep else ''}可投掷{roll}颗骰子{rerolls}次：")
    re_target = re_d_ele.findall(target)
    dict_target = {result[-1]: int(result[:-1]) for result in re_target}
    target_dice_count = sum((dict_target[ele] for ele in dict_target))
    reroll_n = 0
    if keep:
        re_keep = re_d_ele.findall(keep)
        state_dict = {(roll, *[(result[-1], int(result[:-1])) for result in re_keep]): 1}
        keep_dice_count = sum((int(result[:-1]) for result in re_keep))
    else:
        state_dict = {(roll, ): 1}
        keep_dice_count = 0
    max_gar = roll + keep_dice_count - target_dice_count

    while reroll_n < rerolls:
        new_state_dict = {}
        for state in state_dict:
            old_roll = state[0]
            new_weight = state_dict[state] / pow(8, old_roll)
            if len(state) == 2:
                old_keep = {}
            else:
                old_keep = {ele_d_pair[0]: ele_d_pair[1] for ele_d_pair in state[2:]}
            for rerolled_dice in product(*[faces for _ in range(old_roll)]):
                new_roll = old_roll
                new_keep = old_keep.copy()
                for ele in dict_target:
                    _x = dict_target[ele]
                    _y = old_keep.get(ele, 0)
                    if _y < _x:
                        new_ele = rerolled_dice.count(ele)
                        keep_count = min(new_ele, _x - _y)
                        if keep_count:
                            if ele in new_keep:
                                new_keep[ele] += keep_count
                            else:
                                new_keep[ele] = keep_count
                            new_roll -= keep_count
                wild_count = rerolled_dice.count('万')
                if wild_count:
                    if '万' in new_keep:
                        new_keep['万'] += wild_count
                    else:
                        new_keep['万'] = wild_count
                new_roll -= wild_count
                if new_keep:
                    new_state = (new_roll, *[(ele, new_keep[ele]) for ele in new_keep])
                else:
                    new_state = (new_roll,)
                if new_state in new_state_dict:
                    new_state_dict[new_state] += new_weight
                else:
                    new_state_dict[new_state] = new_weight
        state_dict = new_state_dict
        reroll_n += 1
        burn_count = {x: 0 for x in range(roll + 1)}
        for state in state_dict:
            _xxx = state[0] - max_gar
            if _xxx > 0:
                burn_count[_xxx] += state_dict[state]
            else:
                burn_count[0] += state_dict[state]
        exp = sum((n * burn_count[n] for n in burn_count))
        print(f'第{reroll_n}次掷骰后，弃牌期望值 {exp:.3f} 张，张数对应概率：')
        for n in burn_count:
            if burn_count[n] > 0:
                print(f'弃{n}张：{burn_count[n]*100:.4f}%')


def main():
    work(8, '3雷3草', '', 2)
    # work(8, '3雷3草', '', 0)
    # work(8, '3雷3草', '', 4)
    # work(3, '3雷3草', '2万3草')
    # work(4, '3雷3草', '2万2草')
    # work(6, '3雷3草', '2草', 2)
    # work(8, '5水', '', 2)


if __name__ == '__main__':
    main()

