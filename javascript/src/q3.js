import crypto from "crypto";
import Web3 from "web3";
import keccak256 from "keccak256";
import secp256k1 from "secp256k1";

export default function q3() {
    // const privateKey = crypto.randomBytes(32);

    // Manual set private key
    const privateKey = Buffer.from(
        "91138311457C069D22899815C5065D90C28D606255D43347B1A4533ECDBCAB28",
        "hex",
    );

    const ecdh = crypto.createECDH("secp256k1");
    ecdh.setPrivateKey(privateKey);
    let publicKey = ecdh.getPublicKey();

    // 0x04 is the prefix for uncompressed public keys
    // 公開鍵
    console.log("Public Key: " + publicKey.toString("hex").slice(2));

    const signature = secp256k1.ecdsaSign(keccak256("Hello World"), privateKey);
    console.log("Signature: " + signature.signature.toString("hex"));
}
q3();
