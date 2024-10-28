import java.util.Date;
import java.util.List;
import java.util.Optional;

/***
 * Entities
 *
 * User - ADMIN, LENDER
 * Library
 * Book - BookId, Quantity, name, edition, Author, Shelf
 * BookItem - Unique Id, BookId
 * Cost
 * Fine
 *
 * Design a library management system.
 *
 * How would you model books, users, and transactions (borrow/return books)?
 * How would you handle overdue books and fines?
 * How can you support features like searching for a book by title, author, or ISBN?
 */

public class LibraryManagementSystem {

    List<Book> books;

    public static void main(String[] args)
    {

    }

    public void borrowABook(int userId, BookItem bookItem, int noOfDays){
        for(Book book: books){
            if(book.bookId == bookItem.bookId){
                if(book.getQuantity() > 0){
                    book.setQuantity(book.getQuantity() - 1);
                    System.out.println();
                }
            }
        }
    }
}

class User{
    Integer userId;
    UserType userType;
    UserStatus userStatus;
    String name;
    String email;
    String mobile;
}

enum UserType{
    ADMIN,
    BORROWER;
}

enum UserStatus{
    ACTIVE, INACTIVE, BLACK_LISTED;
}

class Book{
    int bookId;
    String name;
    String author;
    private int quantity;
    Optional<String> shelfLocation;
    Cost cost;

    public int getQuantity()
    {
        return quantity;
    }

    public void setQuantity(int quantity)
    {
        this.quantity = quantity;
    }
}

class BookItem{
    int bookItemId;
    int bookId;
}

class Cost{
    int bookId;
    float borrowingCost;
    float finePerOverdueDay;
}

class BorrowTransaction{
    int userId;
    int bookItemId;
    Date date;
}