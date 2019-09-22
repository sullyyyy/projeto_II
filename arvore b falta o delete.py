class BTreeNode(object):
    
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.c    = []
        


class BTree(object):
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t    = t
    
    def search(self, k, x=None):
        
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:    
                i += 1
            if i < len(x.keys) and k == x.keys[i]:       
                return (x, i)
            elif x.leaf:                                
                return None
            else:                                      
                return self.search(k, x.c[i])
        else:                                           
            return self.search(k, self.root)
        
    def insert(self, k):
        r = self.root
        if len(r.keys) == (2*self.t) - 1:    
            s         = BTreeNode()
            self.root = s
            s.c.insert(0, r)                  
            self._split_child(s, 0)            
            self._insert_nonfull(s, k)
        else:
            self._insert_nonfull(r, k)
    
    def _insert_nonfull(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            # insert a key
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i+1] = k
        else:
            
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.c[i].keys) == (2*self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_nonfull(x.c[i], k)
        
    def _split_child(self, x, i):
        t = self.t
        y = x.c[i]
        z = BTreeNode(leaf=y.leaf)
        
        
        x.c.insert(i+1, z)
        x.keys.insert(i, y.keys[t-1])
        
        
        z.keys = y.keys[t:(2*t - 1)]
        y.keys = y.keys[0:(t-1)]
        
       
        if not y.leaf:
            z.c = y.c[t:(2*t)]
            y.c = y.c[0:(t-1)]    
        

    def delete(self, k):
        if self.search(k):
              


#### fim da classe ####

t=int(input("digite a ordem da arvore: "))
arv =  BTree(t)
print("Programa Arvore Binaria")
opcao = 0
while opcao != 5:
     print("***********************************")
     print("Entre com a opcao:")
     print(" --- 1: Inserir")
     print(" --- 2: Excluir")
     print(" --- 3: Pesquisar")
    # print(" --- 4: Exibir")
     print(" --- 5: Sair do programa")
     print("***********************************\n")
     opcao = int(input("-> "))
     if opcao == 1:
          x = int(input(" Informe o valor -> "))
          if arv.search(x) != None:
             print("Chave já existente!")
          else:
              arv.insert(x)
     elif opcao == 2:
          x = int(input(" Informe o valor -> "))
          if arv.search(x) == False:
               print("Chave Inexistente!")
          else:
              arv.delete(x)
     elif opcao == 3:
          x = int(input(" Informe o valor -> "))
          if arv.search(x) != None:
               print("TRUE")
          else:
               print("FALSE")	 
    # elif opcao == 4:
          arv.caminhar()
     elif opcao == 5:
          break


