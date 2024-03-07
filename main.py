
try:
    from web3 import Web3
except Exception as a:
    print(a)

class Chain:

    def __init__(self,name = None,rpc = None) -> None:
        self.name= name
        self.rpc = rpc

    def __str__(self) -> str:
        return str(self.name)
    
proxy= {'https': 'http://kVqHD7sC:G19CZLra@154.196.68.77:64968','http': 'http://kVqHD7sC:G19CZLra@154.196.68.77:64968'}
    
# сети
    
arbitrum = Chain('Arb','https://arb1.arbitrum.io/rpc')
zk = Chain('zk','https://mainnet.era.zksync.io')
erc20 = Chain('eth','https://ethereum-mainnet.core.chainstack.com/70ae3a3e68a6c1ed594168c8a642e4b3')
avax = Chain('Avax','https://avalanche-c-chain.publicnode.com/')
bep20 = Chain('Bep20','https://bsc-dataseed1.defibit.io/')
poligon = Chain('poligon','https://polygon-rpc.com',)
zora = Chain('zora','https://rpc.zora.energy')
scroll = Chain('scroll','https://rpc.scroll.io')

# если хотим добавить сеть то пишем :
# name_set = Chain('name','RPC')

'''
Настройки
'''
chain = scroll # выбираем из списка выше 
file_wal = 'wal.txt' # file wal

'''
готово можно запускать
'''

def chek_tx(adress,chain:Chain):
    if chain.name == 'zora':
        w3 = Web3(provider=Web3.HTTPProvider(chain.rpc,request_kwargs={'proxies': proxy}))
    else:
        w3 = Web3(provider=Web3.HTTPProvider(chain.rpc))
    balanse = w3.eth.get_balance(Web3.to_checksum_address(adress))
    nonce = w3.eth.get_transaction_count(Web3.to_checksum_address(adress))
    return nonce,balanse

def aka(privat,set:Chain):
    w3 = Web3(Web3.HTTPProvider(set.rpc))
    account = w3.eth.account.from_key(privat)
    adress = account.address
    return adress

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
        #adress_wal = aka(wallett(file_wal),zk)
        print(adress_wal,end=' ')
        try:    
            nonse,balanse = chek_tx(adress_wal,chain)
            print(f'nonse {nonse} balanse eth {balanse/10**18}')
        except Exception as a:
            nonse = 0
            print(a)
            write_t(adress_wal+' проверить')
        t= f'{adress_wal} {nonse}'
        write_t(t)
        wallett_del(file_wal)

main()