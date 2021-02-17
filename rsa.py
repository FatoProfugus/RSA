import random
import math

def rsa_encryption(plaintext, e, n):
	ciphertext = pow(plaintext, e, n)
	return ciphertext

def rsa_decryption(ciphertext, d, n):
	plaintext = pow(ciphertext, d, n)
	return plaintext

def main():
	public_n = 900348238029332668175881559281442423068410198618801978249457479037932527260331
	public_e = pow(2,16)+1
	plaintext = 39611541800605679895240898832274013906789
	ciphertext = rsa_encryption(plaintext, public_e, public_n)
	print('ciphertext =', ciphertext)

	p = 929960838713976909720407931803976852619
	q = 808840137850295240473898249118645909517
	n = p*q
	print('n =', n)

	totient_n = (p-1)*(q-1)
	print('totient_n =', totient_n)

	e = pow(2, 16)+1
	d = pow(e, -1, totient_n)
	ciphertext = 159734044950403172452950888182831615189169981060911046776030041921878667289492
	plaintext = rsa_decryption(ciphertext, d, n)
	print('decrypted question =', plaintext)

if __name__ == '__main__':
	main()