from pydantic import BaseModel

class ModelInput(BaseModel):
    vedadc_n:int
    vantig_n:int
    vnline_n:int
    vgamma_c:str
    veaseg_c:bool
    vctcpl_n:int
    vccdeu_n:int
    ttkbco_n:int