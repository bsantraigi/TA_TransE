import torch
import torch.autograd as autograd
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.nn import init

USE_CUDA = torch.cuda.is_available()
if USE_CUDA:
	longTensor = torch.cuda.LongTensor
	floatTensor = torch.cuda.FloatTensor

else:
	longTensor = torch.LongTensor
	floatTensor = torch.FloatTensor

class marginLoss(nn.Module):
	def __init__(self):
		super(marginLoss, self).__init__()

	def forward(self, pos, neg, margin):
		# print("---------------------")
		# print(pos[:20])
		# print(neg[:20])
		# exit()
		zero_tensor = floatTensor(pos.size())
		zero_tensor.zero_()
		zero_tensor = autograd.Variable(zero_tensor)
		return torch.sum(torch.max(pos - neg + margin, zero_tensor))

def orthogonalLoss(rel_embeddings, norm_embeddings):
	return torch.sum(torch.sum(norm_embeddings * rel_embeddings, dim=1, keepdim=True) ** 2 / torch.sum(rel_embeddings ** 2, dim=1, keepdim=True))

def normLoss(embeddings, dim=1):
	# print(embeddings.shape)
	# exit()
	norm = torch.sum(embeddings ** 2, dim=dim, keepdim=True)
	# print(norm.shape)
	# exit()
	return torch.sum(torch.max(norm - autograd.Variable(floatTensor([1.0])), autograd.Variable(floatTensor([0.0]))))

def regulLoss(embeddings):
	return torch.mean(embeddings ** 2)

class binaryCrossLoss(nn.Module):
	def __init__(self):
		super(binaryCrossLoss, self).__init__()

	# def forward(self, pos, neg):
		# print(pos.shape)
		# exit()
		# pos_labels = floatTensor(pos.shape[0])
		# # print(pos_labels.shape)
		# # nn.init.ones_(pos_labels)
		# neg_labels = floatTensor(neg.size())
		# neg_labels.zero_()
		# pos_labels = floatTensor(pos.size())
		# pos_labels.zero_()
		# pos_labels = pos_labels + 1
		# labels = torch.cat((pos_labels, neg_labels))


		# m = nn.Sigmoid()
		# loss = nn.BCELoss()
		# output = F.binary_cross_entropy_with_logits(torch.cat((pos , neg)), labels)
		# return output

	# 	# return F.binary_cross_entropy_with_logits(torch.cat((pos, neg)), labels)
	def forward(self, pos, neg):
		# pos_labels = floatTensor(pos.shape[0])
		# nn.init.ones_(pos_labels)
		# torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
		pos_labels = torch.tensor([1]*len(pos), requires_grad=False, dtype=torch.float32).cuda()
		neg_labels = torch.tensor([0]*len(neg), requires_grad=False, dtype=torch.float32).cuda()
		# neg_labels = floatTensor(neg.shape[0])
		# nn.init.zeros_(neg_labels)
		# print(pos_labels[:20])
		# print(type(pos_labels))
		# exit()
		labels = torch.cat((pos_labels, neg_labels))
		# print(labels)
		# exit()
		return F.binary_cross_entropy_with_logits(torch.cat((pos, neg)), labels)
