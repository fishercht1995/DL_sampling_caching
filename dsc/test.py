"""
Test sampling framework
"""
import module
import argparse
from common import utils

parser = argparse.ArgumentParser(description='DL sampling Test')
parser.add_argument('--dataset', type=str, default="cifar10", help='Dataset: e.g., cifar10')
parser.add_argument('--module', type=str, default='resnet20', help='Module, see available_modules')
parser.add_argument('--epoch', type=int, default = 1)

args = parser.parse_args()


def run_experiment():
    pass

if __name__ == "__main__":
    run_experiment()

