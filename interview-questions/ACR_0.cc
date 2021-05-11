#include <iostream>
using namespace std;

// 52 total unique cards
// 4 suits: spades, hearts, diamonds, clubs
// 13 ranks of each suit: ace(1)-10, jack, queen, king

// create a new deck with all 52 cards
// deal a card - remove from the "top" deck and return the card
// shuffle the deck - a random permutation of the remaining cards (w/ uniform distribution)

// ANSWER FISHER YATES

struct card {
  std::string suit;
  std::string rank;
};

class PokerDeck
{
public:
  explicit PokerDeck();

  void Shuffle();
  card DealCard();
  
private:
  card GetCard();

  std::vector<card> vector_;
  generator_;
  distribution_;
  index_ind_;
};

PokerDeck::PokerDeck()
  queue_(),
  generator_(),
  distribution_(),
  index_ind_(0)
{
  generator_(distribution_);
  
  for (size_t i = 0; i < NUM_SUITS; ++i)
  {
    for (size_t j = 0; i < NUM_RANKS; ++j)
    {
      vector_.emplace_back(GetCard(i, j));
    }
  }
}

void PokerDeck::Shuffle()
{
  for (size i = 0; i < NUM_SUITS * NUM_RANKS - 1; ++i)
  {
    int j = generator_(i, 51);
    vector_.swap(i, j);
  }
}

card PokerDeck::DealCard()
{
  ret_card = vector_[index_ind_]
  ++index_ind_;
  return ret_card;  
}

card GetCard(size_t i, size_t j)
{
  card n_card;
  
  switch(i)
  {
    case 0:
      n_card.suit = "c";
      break;
    case 1:
      n_card.suit = "d";
      break;
    case 2:
      n_card.suit = "h";
      break;
    case 3:
      n_card.suit = "s";
      break;
  }

  if (j <= 9)
  {
    n_card.rank = std::to_string(j);
  }
  else
  {
    switch(j)
    {
      case 10:
        n_card.rank = "j";
        break;
      case 11:
        n_card.rank = "q";
        break;
      case 12:
        n_card.rank = "k";
        break;
    }
  }  
  
  return n_card.rank;
}