{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyN0d0CnwHa2/OkkNuklVWRw"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":5,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"p1cNmMOgqxN0","executionInfo":{"status":"ok","timestamp":1684297298464,"user_tz":-540,"elapsed":1524,"user":{"displayName":"이규영","userId":"12026773311111870199"}},"outputId":"bdbf1969-052b-435c-b56d-0cd0c1f721d0"},"outputs":[{"output_type":"stream","name":"stdout","text":["(75, 1)\n"]}],"source":["# 데이터 전처리 및 분할\n","from sklearn.preprocessing import StandardScaler\n","from sklearn.model_selection import train_test_split\n","class Dataset():\n","  def __init__(self,X,y,random_state = 42,scaled=True):\n","    self.X = X\n","    self.y = y\n","    self.random_state = random_state\n","    self.scaled = scaled\n","    self.split()\n","  def split(self):\n","    X = self.X\n","    y = self.y\n","    scaled = self.scaled\n","    random_state = self.random_state\n","    x_train,x_test,y_train,y_test = train_test_split(X,y,random_state=random_state)\n","    if scaled:\n","      ss = StandardScaler()\n","      ss.fit(x_train)\n","      x_train = ss.transform(x_train)\n","      x_test = ss.transform(x_test)\n","    self.x_train = x_train\n","    self.x_test = x_test\n","    self.y_train = y_train\n","    self.y_test = y_test\n","\n","import numpy as np\n","if __name__ == '__main__':\n","  X = np.arange(100).reshape(-1,1)    \n","  y = np.zeros(100)\n","  data = Dataset(X,y)\n","  print(data.x_train.shape)\n"]},{"cell_type":"code","source":[],"metadata":{"id":"aFBNG6Ptq55m"},"execution_count":null,"outputs":[]}]}