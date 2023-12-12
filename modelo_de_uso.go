var Game int
var player1_acao string
var player2_acao string
var player1_pontos int = 0
var player2_pontos int = 0
var player1_games int = 0
var player2_games int = 0
Game = 1
while Game > 0{
	while player2_games < 6 && player1_games < 6{
		player1_pontos = 0
		player2_pontos = 0
		while player1_pontos < 46 && player2_pontos < 46{
			player1_acao = Scanln()
			if player1_acao == "venceu"{
				player1_pontos += 15
			}
			player2_acao = Scanln()
			if player2_acao == "venceu"{
				player2_pontos += 15
			}
			Println(player1_pontos)
			Println(player2_pontos)


		}
		if player1_pontos > 46{
			player1_games = player1_games + 1
		}else{
			player2_games = player2_games + 1
		}
		Println("Player 1 games")
		Println(player1_games)
		Println("Player 2 games")
		Println(player2_games)

	}
	if player1_games > 5{
		Println("Player 1 venceu")
	}else{
		Println("Player 2 venceu")
	}
	Game = 0
	
}

