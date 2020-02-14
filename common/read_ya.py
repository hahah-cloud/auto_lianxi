import yaml
import os
def readyml(yamlPath):
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：")
    f=open(yamlPath,"r",encoding="utf-8")
    cfg=f.read()
    d=yaml.load(cfg)
    print("读取的测试文件数据：%s"%d)
    return d


if __name__ == '__main__':
    data=readyml("test_da.yml")["update_info"]
    print(data)