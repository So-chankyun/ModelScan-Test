'''
.model, safetensors 확장자를 가진 모델 파일을 pickle 파일로 변환

일단 .safetensors -> pickle만 시도해보자.

converter : abstract class

~converter : implement class

우선 각 함수로 만들고 나중에 쪼갤것.
'''
# from keras.models import load_model
from safetensors.torch import load_file

# 1. .model -> .pickle
def model_to_pickle(path:str,name:str):
    '''
    description:
        
    param:
        path(str) : 
    return:
    '''

    # .model 파일 로드
    model = load_model('path_to_model.model')

    return 

# 2. .safetensors -> .pickle    
def st_to_pickle(path:str,name:str):

    # 모델 가중치 로드
    state_dict = load_file("path_to_model.safetensors")

    model = MyModel()
    model.load_state_dict(state_dict)

    return