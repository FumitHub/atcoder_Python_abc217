import math
# カットした木材の長さを出力する。
def print_length_Woods(len_wood, len_query):
    # 木材の長さリスト
    list_len = [len_wood]
    for _ in range(len_query):
        c, x = map(int, input().split())
        # cが2の時、xメートルのところの木材の長さを出力する。
        if c == 2:
            len_tmp = 0
            for i in range(len(list_len)):
                len_tmp += list_len[i]
                if len_tmp >= x:
                    print(list_len[i])
                    break
        else:
            # 木材をカットする。
            len_tmp = 0
            for j in range(len(list_len)):
                len_tmp += list_len[j]
                if len_tmp >= x:
                    if j == 0:
                        list_len[j] = x
                    else:
                        list_len[j] = x - sum(list_len[:j])
                    list_len.insert(j+1, len_tmp - sum(list_len[:j+1]))
                    break

l, q = map(int, input().split())
print_length_Woods(l, q)

