from torch import nn
from torchvision import models


class AkhundModel(nn.Module):
    def __init__(self, num_classes):
        super(AkhundModel, self).__init__()
        self.resnet101 = models.resnet101(weights=models.ResNet101_Weights.DEFAULT)
        self.resnet101.fc = nn.Linear(in_features=2048, out_features=1024, bias=True)
        self.dropout = nn.Dropout(p=.2)
        self.classifier = nn.Linear(in_features=1024, out_features=num_classes, bias=True)

        for param in self.resnet101.parameters():
            param.requires_grad = False

        self.resnet101.fc.requires_grad = True

    def forward(self, x):
        x = self.resnet101(x)
        x = self.dropout(x)
        x = self.classifier(x)
        return x