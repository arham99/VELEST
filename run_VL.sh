echo "============"
echo "Script to Collect Stattistic result From NonLinLoc - Global mode"
echo "Developed by Arham Zakki Edelo TG-ITS"
echo "Email_1: azedelo1999@gmail.com"
echo "Email_2: edelo.arham@gmail.com"

echo
echo "IMPORTANT"
echo "   1. Taruh script run_VL.SH dan Script COLLECT_VELEST.py ini pada directory yang sama dengan data yang akan di collect"
echo "   2. Harus terinstall python3 dengan library pandas "
echo

#PS_VIEWER=ghostview

echo
python3 ./VELEST_COLLLECT.py

echo "!!!!NOTE!!!!!!"
echo "  1. SETELAH INI WAJIB GANTI KODE STASIUN PADA FILE OUTPUT .CNV DENGAN INTEGER (ANGKA) AGAR DAPAT DIBACA OLEH VELEST"
echo "  2. DISARANKAN MENGGUNAKAN TEXT EDITOR SEPERTI KATE, SUBLIME TEXT, NOTEPAD++, ATOM, DLL"
echo "  3. PROSES FIND & REPLACE DENGAN TEXT EDITOR HARUS MEMPERTAHANKAN FORMAT AWAL YANG DIHASILKAN TERMASUK SPASINYA   !!!! JANGAN RUBAH FORMAT BAHKAN SPASI SEKLAIPUN!!!"
