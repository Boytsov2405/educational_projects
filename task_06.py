class WrongNumberOfPlayersError(Exception):
    def __init__(self, message="Неправильное количество игроков!"):
        super().__init__(message)
class NoSuchStrategyError(Exception):
    def __init__(self, message="Стратегия должна быть одной из 'R', 'P', 'S'!"):
        super().__init__(message)
def rps_game_winner(_game:list) -> str:
    if not isinstance(_game, list) or len(_game) != 2:
       raise WrongNumberOfPlayersError()
    _player_choose = []
    for _player in _game:
        if not isinstance(_player, list) or len(_player) != 2:
            raise WrongNumberOfPlayersError()
        if not isinstance(_player[1], str):
            raise NoSuchStrategyError()
        _player_choose.append(_player[1].strip().upper())
        if  _player_choose[-1] not in {'R','P','S'}:
           raise NoSuchStrategyError()
    if(_player_choose[0] == _player_choose[1]):
        return f"{_game[0][0]} {_player_choose[0]}";
    if(_player_choose[0], _player_choose[1]) in  {('P','R'), ('S','P'), ('R','S')}:
        return f"{_game[0][0]} {_player_choose[0]}";
    return f"{_game[1][0]} {_player_choose[1]}";
    
def print_rps(_game):
    try:
        print(rps_game_winner(_game))
    except WrongNumberOfPlayersError as e:
        print(e)
    except NoSuchStrategyError as e:
        print(e)
    
print_rps([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #=> WrongNumberOfPlayersError
print_rps([['player1', 'P'], ['player2', 'A']]) #=> NoSuchStrategyError
print_rps([['player1', 'P'], ['player2', 'S']]) #=> 'player2 S'
print_rps([['player1', 'P'], ['player2', 'P']]) #=> 'player1 P'