# class Dsx():
#     name = '戴师兄'
#     time = '两年半'
#     age = 18
#     def hello(self):
#         print('各位观众老爷你们好呀😉，我是{}，今年的我{}岁，是一名练习时长{}的高质量分析师'.format(self.name,self.age,self.time))
#     def singing(self):
#         print('''   
#             🤓       我晒干了沉默~♪
#           [📳 ■◣
#          /ア|□■\\◣
#           /■—◥■◤
#          /■ | 👈■
#           / /| |
#           \\\\  \\\\\
         
#            \\\\  \\\\\
          
#          ◢■ ◢■
#          我晒干了沉默~♪
#          悔得很冲动~♫
#          就算这是做错~♬
#          也只是怕错过~♩
#          在一起 叫 梦~♫
#          分开了 叫 痛~♫
#          是不是说没有做完  的  梦  最  痛~♪
#          ''')
def hello():
    name = '戴师兄'
    age = 18
    time = '2年半'
    print('各位观众老爷你们好呀😉，我是{}，今年的我{}岁，是一名练习时长{}的高质量分析师'.format(name,age,time))
    
def singing():
    print('''   
                                                                        🤓         我晒干了沉默~♪
                                                                      [📳 ■◣        悔得很冲动~♫
                                                                     /ア|□■\\◣      就算这是做错~♬
                                                                      /■—◥■◤      也只是怕错过~♩
                                                                     /■ | 👈■       在一起 叫 梦~♫
                                                                      / /| |         分开了 叫 痛~♫
                                                                      \\\\  \\\\      是不是说没有做完  的  梦  最  痛~♪                                                                               
                                                                       \\\\  \\\\\

                                                                     ◢■ ◢■                             
                                                                     
     ''')
    from IPython.display import Markdown
    return Markdown(filename='hight_quality.md')