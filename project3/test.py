# minist 用MLP实现，MLP也是使用pytorch实现的
import torchvision
import torch
from torchvision import datasets, transforms
from torch.autograd import Variable
import torch.optim as optim
from project3.agent import Model
import time

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize((0.5,), (0.5,))])

# 下载数据集
data_train = torch.load("data.pth")

data_test = torch.load("data.pth")
# 装载数据


num_i = 256  # 输入层节点数
num_h = 96  # 隐含层节点数
num_o = 32  # 输出层节点数
num_p = 10
batch_size = 64


model = Model(num_i, num_h, num_o,num_p)
cost = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())
epochs = 5
for epoch in range(epochs):
    sum_loss = 0
    train_correct = 0
    for i in range(len(data_train["feature"])):
        if i%1000==0:
            print(i)
        inputs = data_train["feature"][i]
        labels = data_train["label"][i]  # inputs 维度：[64,1,28,28]
        #     print(inputs.shape)
        #inputs = torch.flatten(inputs, start_dim=1)  # 展平数据，转化为[64,784]
        #     print(inputs.shape)
        outputs = model(inputs)
        optimizer.zero_grad()
        loss = cost(outputs, labels)
        loss.backward()
        optimizer.step()
        #print(outputs.data)
        _, id = torch.max(outputs.data, 0)
        sum_loss += loss.data
        #print(id)
        #print(labels.data)
        #print("---")
        train_correct += torch.sum(id == labels.data)
    print(str(epoch)+":"+str(epochs))
    print('        correct:%.03f%%' % (100 * train_correct / len(data_train["feature"])))
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
torch.save(model, 'model.pth')
model.eval()
test_correct = 0

model = torch.load('model.pth')
for i in range(len(data_test["feature"])):
    if i % 1000 == 0:
        print(i)
    inputs = data_test["feature"][i]
    labels = data_test["label"][i]  # inputs 维度：[64,1,28,28]
    outputs = model(inputs)
    _, id = torch.max(outputs.data, 0)
    test_correct += torch.sum(id == labels.data)
print("correct:%.3f%%" % (100 * test_correct / len(data_train["feature"])))