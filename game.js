class Deck {
	constructor() {
		this.deck = [];
		this.dealt_cards = [];
	}

	generate_deck() {
		let card = (suit, value) => {
			let name = value + ' of ' + suit;
			return { name: name, suit: suit, value: value };
		};

		let values = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ];
		let suits = [ 'Clubs', 'Diamonds', 'Spades', 'Hearts' ];

		for (let s = 0; s < suits.length; s++) {
			for (let v = 0; v < values.length; v++) {
				this.deck.push(card(suits[s], values[v]));
			}
		}
	}
	print_deck() {
		if (this.deck.length == 0) {
			console.log('The deck has been generated');
		} else {
			for (let c = 0; c < this.deck.length; c++) {
				console.log(this.deck[c]);
			}
		}
	}

	shuffle() {
		let current_id = this.deck.length,
			temp_val,
			rand_id;

		while (0 != current_id) {
			rand_id = Math.floor(Math.random() * current_id);
			current_id -= 1;
			temp_val = this.deck[current_id];
			this.deck[current_id] = this.deck[rand_id];
			this.deck[rand_id] = temp_val;
		}
	}

	deal(num_cards) {
		let cards = [];

		for (let c = 0; c < num_cards; c++) {
			let dealt_card = this.deck.shift();
			cards.push(dealt_card);
			this.dealt_cards.push(dealt_card);
		}
		return cards;
	}

	replace() {
		this.deck.unshift(this.deal_cards.shift());
	}

	clear_deck() {
		this.deck = [];
	}
}

deck = new Deck();

deck.generate_deck();

deck.shuffle();
//deck.print_deck();
console.log(deck.deal(4));
