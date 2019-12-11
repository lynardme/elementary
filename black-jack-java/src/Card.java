/**
 * An implementation of a card type
 * 
 * @author Lynard
 *
 */
public class Card {
	
	/**
	 * One of the four valid suits for this card
	 */
	private Suit mySuit;

	/**
	 * The number of this card, where Ace: 1, Jack-King: 11-13
	 */
	private int myNumber;
	
	/**
	 * Card Constructor
	 * 
	 * @param aSuit
	 * @param aNumber
	 */
	public Card(Suit aSuit, int aNumber) {
		this.mySuit = aSuit;
		this.myNumber = aNumber;
	}

	public Suit getMySuit() {
		return mySuit;
	}

	public void setMySuit(Suit mySuit) {
		this.mySuit = mySuit;
	}

	public int getMyNumber() {
		return myNumber;
	}

	public void setMyNumber(int myNumber) {
		this.myNumber = myNumber;
	}
	
}
