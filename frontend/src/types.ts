export type Beer = {
  id: string
  name: string
  type: string
  stock: number
  price: number
}

export type Customer = {
  name: string
}

export type Billing = {
  totalBilling: number
  billingByCustomer: BillingByCustomer
  customers: number
  totalDividedBetweenCustomers: number
}

type BillingByCustomer = {
  [key: string]: number
}