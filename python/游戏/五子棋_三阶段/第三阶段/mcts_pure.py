# -*- coding: utf-8 -*-
"""
A pure implementation of the Monte Carlo Tree Search (MCTS)

"""
from game import Board
import numpy as np
import copy
from operator import itemgetter


def rollout_policy_fn(board:Board):#!快速走子策略（Rollout policy）
    """a coarse, fast version of policy_fn used in the rollout phase."""
    # rollout randomly
    action_probs = np.random.rand(len(board.availables))
    return zip(board.availables, action_probs)




def policy_value_fn(board: Board):#! 返回当前棋盘每个可以下的点和先验概率组成的元祖
    """a function that takes in a state and outputs a list of (action, probability)
    tuples and a score for the state"""
    # return uniform probabilities and 0 score for pure MCTS
    action_probs = np.ones(len(board.availables))/len(board.availables)
    return zip(board.availables, action_probs), 0


class TreeNode(object):
    """A node in the MCTS tree. Each node keeps track of its own value Q,
    prior probability P, and its visit-count-adjusted prior score u.
    """

    def __init__(self, parent, prior_p):
        self._parent = parent
        self._children = {}  # a map  action : TreeNode
        self._n_visits = 0
        self._Q = 0
        self._u = 0
        self._P = prior_p

    def expand(self, action_priors):
        """Expand tree by creating new children.
        action_priors: a list of tuples of actions and their prior probability
            according to the policy function.
        """
        for action, prob in action_priors:
            if action not in self._children:#这里相当于 if action not in self._children.keys()
                self._children[action] = TreeNode(self, prob)#! 新建的节点的父节点就是当前节点


    def _get_value(self, c_puct):
        """Calculate and return the value for this node.
        It is a combination of leaf evaluations Q, and this node's prior
        adjusted for its visit count, u.
        c_puct: a number in (0, inf) controlling the relative impact of
            value Q, and prior probability P, on this node's score.
        """
        #!搜索树会在这个值较大时趋向于向未模拟过的落子点探索，在其较小时则会快速收敛。
        # 这种搜索方式最初会倾向于先验概率P（s，d）较高和节点访问次数C（s，d）较低的落子动作，
        # 之后会渐渐倾向于平均行动价值Q（s，d）较高的落子动作。式中表示根节点的访问次数；
        # c（s，d）表示当前叶子节点的访问次数：P（s，d）为深度神经网络的策略输出对应动作d的概率值.
        self._u = (c_puct * self._P *
                   np.sqrt(self._parent._n_visits) / (1 + self._n_visits))
        return self._Q + self._u
    
    
    def select(self, c_puct):#通过_get_value函数找到“最值得搜索的子节点”
        """Select action among children that gives maximum action value Q
        plus bonus u(P).
        Return: A tuple of (action, next_node)
        """
        #!max函数中key参数的作用
        #正常元组不能用max函数 传入key参数后就可以了
        return max(self._children.items(),
                   key=lambda act_node: act_node[1]._get_value(c_puct))
        

    
    
    def _update(self, leaf_value):
        """Update node values from leaf evaluation.
        leaf_value: the value of subtree evaluation from the current player's
            perspective.
        """
        # Count visit.
        self._n_visits += 1
        # Update Q, a running average of values for all visits.
        self._Q += 1.0*(leaf_value - self._Q) / self._n_visits

    def update_recursive(self, leaf_value):#通过_update函数更新祖先
        """Like a call to update(), but applied recursively for all ancestors.
        """
        # If it is not root, this node's parent should be updated first.
        if self._parent:
            self._parent.update_recursive(-leaf_value)#! 注意这里有一个-号 因为他的父亲是对手 如果孩子分高 那么他的对手相应的分数应该降低
        self._update(leaf_value)


    def is_leaf(self):
        """Check if leaf node (i.e. no nodes below this have been expanded).
        """
        return self._children == {}

    def is_root(self):
        return self._parent is None





class MCTS(object):
    """A simple implementation of Monte Carlo Tree Search."""

    def __init__(self, policy_value_fn, c_puct=5, n_playout=10000):
        """
        policy_value_fn: a function that takes in a board state and outputs
            a list of (action, probability) tuples and also a score in [-1, 1]
            (i.e. the expected value of the end game score from the current
            player's perspective) for the current player.
        c_puct: a number in (0, inf) that controls how quickly exploration
            converges to the maximum-value policy. A higher value means
            relying on the prior more.
        """
        self._root = TreeNode(None, 1.0)
        self._policy = policy_value_fn
        self._c_puct = c_puct
        self._n_playout = n_playout

    def _playout(self, state): #! 蒙特卡洛四步的实现 每个步骤都对应一个函数 这个函数聚合了四个函数 实现了MCTS
        """Run a single playout from the root to the leaf, getting a value at
        the leaf and propagating it back through its parents.
        State is modified in-place, so a copy must be provided.
        """
        node = self._root
        #todo step1: selection
#第一步是选择(Selection):这一步会从根节点开始，每次都选一个“最值得搜索的子节点”，
# 一般使用最大置信上界（UCT）选择分数最高的节点，
# 直到来到一个“存在未扩展的子节点”的节点
        while(1):
            if node.is_leaf():

                break
            # Greedily select next move.
            action, node = node.select(self._c_puct)
            state.do_move(action)


        #todo step2: expansion
        action_probs, _ = self._policy(state)
        # Check for end of game
        end, winner = state.game_end()
        
        if not end:
            node.expand(action_probs)
        
        #todo step3: simulation
        # Evaluate the leaf node by random rollout
        leaf_value = self._evaluate_rollout(state)#!快速走子策略（Rollout policy）
        #第三步是仿真(Simulation)，从上面这个没有试过的着法开始，用一个简单策略比如快速走子策略（Rollout policy）走到底，得到一个胜负结果
        
        #todo step4: update
        # Update value and visit count of nodes in this traversal.
        node.update_recursive( -leaf_value )


    def _evaluate_rollout(self, state, limit=1000):
        """Use the rollout policy to play until the end of the game,
        returning +1 if the current player wins, -1 if the opponent wins,
        and 0 if it is a tie.
        """
        player = state.get_current_player()
        for i in range(limit):
            end, winner = state.game_end()
            if end:
                break
            action_probs = rollout_policy_fn(state)#! 见程序开头的快速走子策略
            max_action = max(action_probs, key=itemgetter(1))[0]
            state.do_move(max_action)
        else:
            # If no break from the loop, issue a warning.
            print("WARNING: rollout reached move limit")
        if winner == -1:  # tie
            return 0
        else:
            return 1 if winner == player else -1


    def get_move(self, state):#! 找到最优解 核心函数 实际上就是self._n_playout次 _playout函数 并找到其中的最优解了
        """Runs all playouts sequentially and returns the most visited action.
        state: the current game state

        Return: the selected action
        """
        for n in range(self._n_playout):#! 注意每一次模拟的数据已经被存起来了 但是每一次模拟state会被重置
            state_copy = copy.deepcopy(state)#! state是一个Board对象 里面的所有东西全都被复制过来了
            self._playout(state_copy)#! 执行那4步的流程,执行的次数为self._n_playout 次数越多越准确
            
        #! 根据根节点的子节点的访问量，选择最佳的动作
        return max(self._root._children.items(),
                   key=lambda act_node: act_node[1]._n_visits)[0]

    def update_with_move(self, last_move):
# 当使用蒙特卡洛树搜索执行完一个动作时，博弈状态往前推进了一步，新的状态为对手的起始状态。
# 当对手也完成落子时，新的状态即为新一轮蒙特卡洛树搜索的根节点（起始状态）。
# 而如果对手的落子选择在上一次模拟的情况之内，可以从上一轮展开的博弈树中截取相应的子树成为新的博弈树，
# 这样就实现了博弈树模拟结果的复用，提高了模拟的效率。当对手的落子选择不在上一次模拟情况内的时候，
# 则需要构建一颗新的博弈树，上一轮的模拟结果均被舍弃。
        """Step forward in the tree, keeping everything we already know
        about the subtree.
        """
        if last_move in self._root._children:
            self._root = self._root._children[last_move]
            self._root._parent = None
        else:
            self._root = TreeNode(None, 1.0)

    def __str__(self):
        return "MCTS"


class MCTSPlayer(object):
    """AI player based on MCTS"""
    def __init__(self, c_puct=5, n_playout=2000):
        self.mcts = MCTS(policy_value_fn, c_puct, n_playout)

    def set_player_ind(self, p):
        self.player = p

    def reset_player(self):
        self.mcts.update_with_move(-1)

    def get_action(self, board):
        sensible_moves = board.availables
        if len(sensible_moves) > 0:
            move = self.mcts. get_move(board)
            self.mcts.update_with_move(-1)#!  重置
            return move
        else:
            print("WARNING: the board is full")

    def __str__(self):
        return "MCTS {}".format(self.player)
