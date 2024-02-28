import { useEffect, useState } from "react";
import "./App.css";
import { Billing } from "./types";

function App() {
  const [billing, setBilling] = useState<Billing>(null as unknown as Billing);
  const [customers, setCustomers] = useState<string[]>([]);
  const [paymentType, setPaymentType] = useState<string>("DIVIDED");

  const fetchBilling = async () => {
    const response = await fetch(
      import.meta.env.VITE_API_URL + "/orders/billing"
    );
    const data = await response.json();
    const customers = Object.keys(data.billing.billingByCustomer);
    setBilling(data.billing);
    setCustomers(customers);
  };

  useEffect(() => {
    fetchBilling();
  }, []);

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const form = event.currentTarget;
    const customer = form.customers.value;
    const paymentType = form.payment_type.value;
    await fetch(
      import.meta.env.VITE_API_URL + "/orders/payment",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          customer_name: customer,
          payment_type: paymentType,
          value:
            paymentType === "DIVIDED"
              ? billing.totalDividedBetweenCustomers
              : billing.billingByCustomer[customer],
        }),
      }
    );
    fetchBilling();
  };

  return (
    <div className="container">
      <h1>Billing</h1>
      {billing && billing.totalBilling <= 0 ? (
        <p>No billing yet</p>
      ) : (
        <form onSubmit={handleSubmit}>
          <select name="customers" id="customers">
            {customers.map((customer) => (
              <option key={customer} value={customer}>
                {customer} - {paymentType === "DIVIDED" ? billing.totalDividedBetweenCustomers : billing.billingByCustomer[customer]}
              </option>
            ))}
          </select>
          {billing && (
            <select name="payment_type" id="payment_type" value={paymentType} onChange={(e) => {setPaymentType(e.target.value)}}>
              <option value="DIVIDED">Divided</option>
              <option value="MY_ORDERS">My Orders</option>
            </select>
          )}
          <button type="submit">PAY</button>
        </form>
      )}
    </div>
  );
}

export default App;
