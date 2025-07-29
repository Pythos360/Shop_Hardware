
class addHardware():
    #this class allows the addition of missing hardware parts into the table
    def __init__(self, ui,db, sql):
        self.ui = ui
        self.sql = sql
        self.db = db

        self.ui.addHardwareButton.clicked.connect(self.addHardwareSQL)

    def addHardwareSQL(self):
        # 1) Pull all the details from the UI
        size      = self.ui.sizeEdit.text()
        head      = self.ui.headEdit.text()
        number    = self.ui.mcmasterEdit.text()
        length    = self.ui.lengthEdit.text()
        quantity  = self.ui.quantityEdit.text()
        price     = self.ui.priceEdit.text()
        pkg       = self.ui.pkgEdit.text()
        thread    = self.ui.threadEdit.currentText()
        reorder   = self.ui.reorder.text()

        # 2) Validate / convert types
        try:
            quantity = int(quantity)
        except ValueError:
            print("quantity is not int")
            return

        try:
            price = float(price)
        except ValueError:
            print("price is not float")
            return

        try:
            pkg = int(pkg)
        except ValueError:
            print("pkg is not int")
            return

        try:
            reorder = int(reorder)
        except ValueError:
            print("reorder is not int")
            return

        # 3) Compute your per-unit price (or however you want to name this)
        ourPrice = price / pkg
        print(ourPrice)
        # 4) Prepare a fresh query tied to your DB

        self.sql.prepare("""
            INSERT INTO active_hardware
              (mcmaster_number,
               size,
               head,
               length,
               quantity,
               our_price,
               pkg_qty,
               threading,
               is_active,
               ordernumber,
               tot_price)
            VALUES
              (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """)


        # 5) Bind exactly 10 values, in the same order
        self.sql.addBindValue(number)    # mcmaster_number
        self.sql.addBindValue(size)      # size
        self.sql.addBindValue(head)      # head
        self.sql.addBindValue(length)    # length
        self.sql.addBindValue(quantity)  # quantity
        self.sql.addBindValue(ourPrice)  # our_price (float)
        self.sql.addBindValue(pkg)       # pkg_qty
        self.sql.addBindValue(thread)    # threading
        self.sql.addBindValue(0)         # is_active (default false)
        self.sql.addBindValue(reorder)   # ordernumber
        self.sql.addBindValue(price)

        # 6) Execute and check for errors
        if not self.sql.exec():
            print("Insert failed:", self.sql.lastError().text())
        else:
            print(f"Inserted new hardware record for {number}")

        # (Optionally) clear the form or refresh your view here








