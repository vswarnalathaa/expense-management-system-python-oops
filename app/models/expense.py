from datetime import date, datetime
from uuid import uuid4,UUID


class Expense:
   def __init__(
         self,
         amount:float,
         e_date: str,
         category: str,
         description: str,
         payment_method: str,
         e_id = None,
         created_at = None,
        ):
      if e_id is None:
          self.e_id = uuid4()
      else:
          self.e_id = e_id

      self.amount = amount
      self.e_date = e_date
      self.category = category
      self.description = description
      self.payment_method = payment_method
      if created_at is None:
        self.created_at = datetime.now()
      else:
          self.created_at = created_at


   def display(self):
      print(f"ID : {str(self.e_id)}")
      print(f"Amount : {self.amount}")
      print(f"e_date : {self.e_date}")
      print(f"category : {self.category}")
      print(f"description : {self.description}")
      print(f"payment_method : {self.payment_method}")
      print(f"Created_at : {self.created_at}")

   
   def to_dict(self):
      
        return {
            "e_id": str(self.e_id),
            "amount": self.amount,
            "e_date": self.e_date,
            "category": self.category,
            "description": self.description,
            "payment_method": self.payment_method,
            "created_at": self.created_at.isoformat()
        }
   @classmethod
   def from_dict(cls,exp_dict):
       e_id = UUID(exp_dict["e_id"])
       amount = exp_dict["amount"]
       e_date = exp_dict["e_date"]
       category = exp_dict["category"]
       description = exp_dict["description"]
       payment_method = exp_dict["payment_method"] 
       created_at = datetime.fromisoformat(exp_dict["created_at"])
       
       return cls(
           amount=amount,
           e_date=e_date,
           category=category,
           description=description,
           payment_method=payment_method,
           e_id=e_id,
           created_at=created_at
       )
   
   def compact_display(self):
       return f"{self.e_date} | {self.category} | {self.amount}"
       
             