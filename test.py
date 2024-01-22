"""
Test sampling framework
"""
import module
import argparse

parser = argparse.ArgumentParser(description='DL sampling Test')
parser.add_argument('--dataset', type=str, default="cifar10", help='Dataset: e.g., cifar10')
parser.add_argument('--epoch', type=int, default = 1)


args = parser.parse_args()
print(args.dataset)

