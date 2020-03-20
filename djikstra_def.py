# 辞書の値からキーをリストで返す
def get_keys_from_value(d_, val_):
    return [k for k, v in d_.items() if v == val_]

#costs_辞書の中で、最も値の低いkeyを返す。ただし, processed_リストにあるキーは除く
def get_min_node(costs_, processed_):
    keys_list_ = list(costs_.keys())
    for i in processed_:
        keys_list_.remove(i)
    now_cost_ = costs_[keys_list_[0]]
    for keys_ in keys_list_[1:]:
        now_cost_ = min([now_cost_, costs_[keys_]])
    return get_keys_from_value(costs_, now_cost_)

#ダイクストラ法
#graph_は二重辞書。１段目は全ノードをkeyに持つ。
#二つ目は１段目のノードがから接続されているノードへのキーとコストを持つ
def Dijks(graph_):
    processed_ = [] #処理済みノードを格納

    parents_ = {} #そのノードへの直前のノードを格納
    costs_ = {} #各ノードへのコストを格納
    for keys in graph_.keys():
        parents_[keys] = ''
        costs_[keys] = 99999 #各ノードのコストを初期化

    #スタート地点を処理
    for i in graph_['S'].keys():
        costs_[i] = graph_['S'][i]
        parents_[i] = 'S'

    while len(processed_)<len(graph_.keys()):
        #costsの中で最もコストの低いノードをリストで取り出す
        tmp_node = get_min_node(costs_, processed_)
        for node in tmp_node:
            #選んだノードからいけるノードを処理する
            for key in graph_[node].keys():
                #今回の経路のコストが、以前に求めた経路よりも小さければ更新する
                if costs_[key] > costs_[node]+graph_[node][key]:
                    costs_[key] = costs_[node]+graph_[node][key]
                    parents_[key] = node

            processed_.append(node)

    return costs_, parents_

def shortest_root(parents_, target_='Fin'):
    root_ = [target_]
    now_ = target_
    while now_ != 'S':
        root_.append(parents_[now_])
        now_ = parents_[now_]
    return root_[::-1]
