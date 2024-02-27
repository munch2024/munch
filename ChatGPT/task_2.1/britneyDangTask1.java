private Optional<Player> playerWithMost(Predicate<Card> condition) {
    Player scoringPlayer = null;
    int maxCount = 0;

    for (Player p : players) {
        int count = 0;

        for (Card c : p.pile) {
            if (condition.test(c)) {
                count++;
            }
        }

        if (count > maxCount) {
            scoringPlayer = p;
            maxCount = count;
        } else if (count == maxCount) {
            scoringPlayer = null;
        }
    }

    return Optional.ofNullable(scoringPlayer);
}


private void updateScores() {
    for (Player p : players) {
        p.score = p.scopas;
    }

    playerWithMost(p -> true).ifPresent(p -> p.score += 1); // most cards
    playerWithMost(c -> c.is(Card.Value.SEVEN)).ifPresent(p -> p.score += 1); // most sevens
    playerWithMost(c -> c.is(Card.Suit.SPADES)).ifPresent(p -> p.score += 1); // most spades

}
