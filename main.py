from web3 import Web3

class Chain:

    def __init__(self,name = None,rpc = None) -> None:
        self.name= name
        self.rpc = rpc

    def __str__(self) -> str:
        return str(self.name)
    
# сети
    
arbitrum = Chain('Arb','https://arb1.arbitrum.io/rpc')
zk = Chain('zk','https://mainnet.era.zksync.io')
erc20 = Chain('eth','https://rpc.ankr.com/eth')
avax = Chain('Avax','https://avalanche-c-chain.publicnode.com/')
bep20 = Chain('Bep20','https://bsc-dataseed1.defibit.io/')
poligon = Chain('poligon','https://polygon-rpc.com',)

# если хотим добавить сеть то пишем :
# name_set = Chain('name','RPC')

'''
Настройки
'''
chain = zk # выбираем из списка выше 
file_wal = 'wal.txt' # file wal

'''
готово можно запускать
'''

def chek_tx(adress,chain):
    w3 = Web3(provider=Web3.HTTPProvider(chain.rpc))
    nonce = w3.eth.get_transaction_count(adress)
    return nonce

def wallett(file):
    private = open(file,'r').read().splitlines()
    wallet = private[00]
    return wallet

def wallett_del(file):
    ish = open(file,'r').readlines()
    del ish[00]
    with open(file, "w") as file:
        file.writelines(ish)

def write_t(text):
    with open('wal_true.txt', 'a') as f:
        f.write(f'{text}\n')

def main():
    while True:
        adress_wal = wallett(file_wal)
        print(adress_wal,end=' ')
        try:    
            nonse = chek_tx(adress_wal,chain)
            print(nonse)
        except Exception as a:
            nonse = 0
            print(a)
            write_t(t+' проверить')
        t= f'{adress_wal} {nonse}'
        write_t(t)
        wallett_del(file_wal)

main()