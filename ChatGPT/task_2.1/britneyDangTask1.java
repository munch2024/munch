private Optional<Player> playerWithMostCards()
{
    Player scoringPlayer = null;
    int maxCount = 0;

    for(Player p : players)
    {
        final int count = p.pile.size();

        if(count > maxCount)
        {
            scoringPlayer = p;
            maxCount = count;
        }
        else if(count == maxCount)
        {
            scoringPlayer = null;
        }
    }

    return Optional.ofNullable(scoringPlayer);
}

private Optional<Player> playerWithMostSevens()
{
    Player scoringPlayer = null;
    int maxCount = 0;

    for(Player p : players)
    {
        int count = 0;

        for(Card c : p.pile)
        {
            if(c.is(Card.Value.SEVEN))
            {
                count++;
            }
        }

        if(count > maxCount)
        {
            scoringPlayer = p;
            maxCount = count;
        }
        else if(count == maxCount)
        {
            scoringPlayer = null;
        }
    }

    return Optional.ofNullable(scoringPlayer);
}

private Optional<Player> playerWithMostSpades()
{
    Player scoringPlayer = null;
    int maxCount = 0;

    for(Player p : players)
    {
        int count = 0;

        for(Card c : p.pile)
        {
            if(c.is(Card.Suit.SPADES))
            {
                count++;
            }
        }

        if(count > maxCount)
        {
            scoringPlayer = p;
            maxCount = count;
        }
        else if(count == maxCount)
        {
            scoringPlayer = null;
        }
    }

    return Optional.ofNullable(scoringPlayer);
}
