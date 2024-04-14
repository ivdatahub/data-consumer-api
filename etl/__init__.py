import requests
from etl.utils.constants import ENDPOINT_LIST_AVALIABLE_PARITYS
from etl.utils.logs import loggingWarn
from etl.jobs.extract.ApiToParquetFile import extraction

mdName = "extract_prepare"

class ExecutePipeline:
    def __init__(self, *xargs) -> None:
        self.params =  list(xargs)
        self.params_count = len(self.params)
        
        totalInvalidParams = 0
        for arg in self.params:
            if not isinstance(arg, str):
                totalInvalidParams += 1
                
        if totalInvalidParams == self.params_count:
            raise TypeError("Invalid parameters")
            
        self.ValidParams = self.ValidParamsForCall()
        self.pipelineExecute()
            
    def ValidParamsForCall(self) -> list:
        valParams = []
        AvaliableList = requests.get(ENDPOINT_LIST_AVALIABLE_PARITYS).json()
        
        for param in self.params:
            if param in AvaliableList:
                valParams.append(param)
            else:
                loggingWarn(f"Param: {param} is not valid for call", mdName)
            
        return valParams
    
    def pipelineExecute(self):
        if self.ValidParams:
            extraction(self.ValidParams)
            # pgLoading()
        else:
            raise KeyError(f"The informed params are not disponible for extract, see avaliable list in: {ENDPOINT_LIST_AVALIABLE_PARITYS}")