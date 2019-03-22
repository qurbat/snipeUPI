## snipeUPI

A script for querying and discovering existing and unclaimed Unified Payment Interface (UPI) Virtual Payment Addresses. The script primarily serves as a Proof of Concept for demonstrating the lack of rate limiting on the API located at: `https://www.swiggy.com/dapi/payment/upi/verify-vpa`

## Usage

**IMPORTANT:** snipeUPI relies on having an authenticated session on the Swiggy website in order to  query virtual payment addresses. Prior to using the script for the first time, remember to replace the placeholder values on `Line 57` with valid cookies from an authenticated session on swiggy.com.

    'Cookie': '_cookie1=value1; _cookie2=value2; _cookie3=value3'

### Querying a single payment address
    snipeUPI.py -a example@handle

![querying a single address](https://i.imgur.com/rqCTACx.png)

### Querying multiple addresses from file

    snipeUPI.py -f example.txt

![querying multiple addresses](https://i.imgur.com/frkfLRC.gif)
## References

 - `example.txt` contains a list of names (adopted from a dataset
   released by Milos Bejda) with varying payment address handles
   attached as suffixes;
 - `example_names_male_sbi.txt` contains a list of names (1,000) with
   `'@sbi'` attached as a suffix;
 - `example_names_female_axisbank.txt` contains a list of names (1,000)
   with `'@axisbank'` attached as a suffix;
 - `vpa_suffixes_list.txt` contains a list of all known payment address
   suffixes for the Unified Payment Interface.

## Limitations

 - It was found that several banks maintain a blacklist of disallowed UPI payment addresses. In such cases, the script will correctly identify that a particular payment address does not exist, however, it will not be able to signal whether or not the address is affected by a bank-specific blacklist (which may make it unavailable for registering).

 - The API  used for querying payment addresses may at any given time (and without forewarning) be removed or otherwise modified in such a way that could incapacitate the functioning and purpose of the script.
