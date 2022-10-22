import crypto from "crypto";
import Web3 from "web3";
import keccak256 from "keccak256";

export default function q2() {
    // const privateKey = crypto.randomBytes(32);

    // Manual set private key
    const privateKey = Buffer.from(
        "91138311457C069D22899815C5065D90C28D606255D43347B1A4533ECDBCAB28",
        "hex",
    );

    // 秘密鍵
    console.log("Private Key: " + privateKey.toString("hex"));

    /////////////////////////////////////////////////////////////////

    const ecdh = crypto.createECDH("secp256k1");
    ecdh.setPrivateKey(privateKey);
    let publicKey = ecdh.getPublicKey();

    // 0x04 is the prefix for uncompressed public keys
    // 公開鍵
    console.log("Public Key: " + publicKey.toString("hex").slice(2));

    /////////////////////////////////////////////////////////////////
    const web3 = new Web3();
    const ethreumAddress = web3.eth.accounts.privateKeyToAccount(
        privateKey.toString("hex"),
    );
    // Ethereum Address
    console.log("Ethereum Address: " + ethreumAddress.address);

    /////////////////////////////////////////////////////////////////
    // 0x is the prefix for hex strings
    const hashedPublicKey = keccak256(
        "0x" + publicKey.toString("hex").slice(2),
    );
    console.log("Hashed Public Key: " + hashedPublicKey.toString("hex"));
    const ethereumAddress = "0x" + hashedPublicKey.toString("hex").slice(24);
    // Ethereum Address
    console.log("Ethereum Address: " + ethereumAddress);
}
q2();
