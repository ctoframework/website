# DKIM

DomainKeys Identified Mail (DKIM) is an email authentication method that helps prevent email spoofing by allowing receiving mail servers to verify that an email was sent from an authorised source and has not been altered in transit. It works by using cryptographic signatures embedded in email headers.

## **How It Works**

1. **Signing Emails**:

   - When an email is sent, the sending mail server generates a unique DKIM signature using a private key.
   - This signature is added as a header to the email and includes a cryptographic hash of specific email components, such as the body and headers.

2. **Publishing the Public Key**:

   - The domain owner publishes the corresponding public key in the domain’s DNS records under a specific DKIM selector.

3. **Verification by Recipients**:
   - When a receiving mail server gets the email, it retrieves the public key from the sender’s DNS records.
   - The server uses this key to decrypt the DKIM signature and verify that the email content matches the original signature.
   - If the verification succeeds, it confirms that the email is genuinely from the claimed domain and has not been modified.

## **Why It Matters**

- **Prevents Email Spoofing**: Ensures emails claiming to be from a domain are actually sent by authorised mail servers.
- **Enhances Deliverability**: Reduces the chances of emails being flagged as spam or phishing.
- **Strengthens Security**: Helps email providers filter out malicious emails more effectively when combined with SPF (Sender Policy Framework) and DMARC (Domain-based Message Authentication, Reporting & Conformance).

DKIM is a crucial layer in email security, ensuring trust and integrity in email communications.
