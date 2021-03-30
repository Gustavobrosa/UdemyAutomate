message =  '''Sorte e escolhas bem feitas

Pessoas consideradas inteligentes dizem que a felicidade é uma idiotice, que pessoas felizes não se deprimem, não têm vida interior, não questionam nada, são uns bobos alegres, enfim, que a felicidade anestesia o cérebro.

Eu acho justamente o contrário: cultivar a infelicidade é que é uma burrice. O que não falta nessa vida é gente sofrendo pelos mais diversos motivos: ganham mal, não têm um amor, padecem de alguma doença, sei lá, cada um sabe o que lhe dói. Todos trazem uns machucados de estimação, você e eu inclusive. No que me diz respeito, dedico a meus machucados um bom tempo de reflexão, mas não vou fechar a cara, entornar uma garrafa de uísque e me considerar uma grande intelectual só porque reflito sobre a miséria humana. Eu reflito sobre a miséria humana e sou muito feliz, e salve a contradição.

Felicidade depende basicamente de duas coisas: sorte e escolhas bem feitas. Tem que ter a sorte de nascer numa família bacana, sorte de ter pais que incentivem a leitura e o esporte, sorte de eles poderem pagar os estudos pra você, sorte por ter saúde. Até aí, conta-se com a providência divina. O resto não é mais da conta do destino: depende das suas escolhas.

Os amigos que você faz, se optou por ser honesto ou ser malandro, se valoriza mais a grana do que a sua paz de espírito, se costuma correr atrás ou desistir dos seus projetos, se nas suas relações afetivas você prioriza a beleza ou as afinidades, se reconhece os momentos de dividir e de silenciar, se sabe a hora de trocar de emprego, se sai do país ou fica, se perdoa seu pai ou preserva a mágoa pro resto da vida, esse tipo de coisa.

A gente é a soma das nossas decisões, todo mundo sabe. Tem gente que é infeliz porque tem um câncer. E outros são infelizes porque cultivam uma preguiça existencial. Os que têm câncer não têm sorte. Mas os outros, sim, têm a sorte de optar. E estes só continuam infelizes se assim escolherem.'''
count = {} 

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print (count)
