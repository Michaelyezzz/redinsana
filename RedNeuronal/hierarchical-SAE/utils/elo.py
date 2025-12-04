class EloRating:
    def __init__(self, k_factor=16, initial_rating=400):
        self.k_factor = k_factor
        self.initial_rating = initial_rating
        self.ratings = {}  # Almacena los ratings de cada modelo
        
    def get_rating(self, player_id):
        """Obtiene el rating de un jugador, si no existe lo inicializa"""
        return self.ratings.setdefault(player_id, self.initial_rating)
        
    def expected_score(self, rating_a, rating_b):
        """Calcula la probabilidad esperada de victoria del jugador A sobre B"""
        return 1 / (1 + 10**((rating_b - rating_a) / 400))
        
    def update_ratings_from_match(self, player_a_id, player_b_id, result):
        """Actualiza ratings basado en el resultado de un partido
        result: 1 si gana A, 0 si gana B, 0.5 si empate"""
        rating_a = self.get_rating(player_a_id)
        rating_b = self.get_rating(player_b_id)
        expected_a = self.expected_score(rating_a, rating_b)
        
        # Calcular el cambio de rating
        if result == 1:  # A gana
            rating_change = self.k_factor * (1 - expected_a)
        elif result == 0:  # B gana
            rating_change = self.k_factor * (0 - expected_a)
        else:  # Empate
            rating_change = self.k_factor * (0.5 - expected_a)
            
        # Actualizar ratings
        self.ratings[player_a_id] = rating_a + rating_change
        self.ratings[player_b_id] = rating_b - rating_change  # El oponente gana/pierde lo opuesto