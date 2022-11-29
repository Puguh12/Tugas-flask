from webbrowser import get
from flask import Flask, render_template, url_for, redirect
from flask import request
import mysql.connector

#from auth import login 
application = Flask(__name__)

def getMysqlConnection():
    return mysql.connector.connect(user='root', host='localhost', port='3306', password='', database='uts')

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html',)

@application.route('/')
@application.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',)

@application.route('/')
@application.route('/anggota')
def anggota():
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from anggota"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('anggota.html', kalimat=output_json)

@application.route('/anggota', methods=['GET','POST'])
def simpan():
    print(request.method)
    if request.method == 'GET':
        return render_template('anggota.html')
    else: 
        request.method == 'POST'
        kode_anggota = request.form['kode_anggota']
        nama_anggota = request.form['nama_anggota']
        jk_anggota = request.form['jk_anggota']
        jurusan_anggota = request.form['jurusan_anggota']
        no_telp_anggota = request.form['no_telp_anggota']
        alamat_anggota = request.form['alamat_anggota']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO anggota (kode_anggota, nama_anggota, jk_anggota, jurusan_anggota, no_telp_anggota, alamat_anggota) VALUES ('"+kode_anggota+"','"+nama_anggota+"','"+jk_anggota+"','"+jurusan_anggota+"','"+no_telp_anggota+"','"+alamat_anggota+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('anggota'))

@application.route('/update', methods=["POST"])
def update():
    id_anggota = request.form['id_anggota']
    kode_anggota = request.form['kode_anggota']
    nama_anggota = request.form['nama_anggota']
    jk_anggota = request.form['jk_anggota']
    jurusan_anggota = request.form['jurusan_anggota']
    no_telp_anggota = request.form['no_telp_anggota']
    alamat_anggota = request.form['alamat_anggota']
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("UPDATE anggota SET kode_anggota=%s,nama_anggota=%s,jk_anggota=%s,jurusan_anggota=%s,no_telp_anggota=%s,alamat_anggota=%s WHERE id_anggota=%s",(kode_anggota,nama_anggota,jk_anggota,jurusan_anggota,no_telp_anggota,alamat_anggota,id_anggota,))
    db.commit()
    return redirect(url_for('anggota'))

@application.route('/hapus/<string:id_anggota>', methods=["GET"])
def hapus(id_anggota):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("DELETE FROM anggota WHERE id_anggota=%s", (id_anggota,))
    db.commit()
    return redirect(url_for('anggota'))


@application.route('/')
@application.route('/buku')
def buku():
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from buku"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('buku.html', kalimat=output_json)

@application.route('/buku', methods=['GET','POST'])
def simpanbuku():
    print(request.method)
    if request.method == 'GET':
        return render_template('buku.html')
    else: 
        request.method == 'POST'
        kode_buku = request.form['kode_buku']
        judul_buku = request.form['judul_buku']
        penulis_buku = request.form['penulis_buku']
        penerbit_buku = request.form['penerbit_buku']
        tahun_penerbit = request.form['tahun_penerbit']
        stok = request.form['stok']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO buku (kode_buku, judul_buku, penulis_buku, penerbit_buku, tahun_penerbit, stok) VALUES ('"+kode_buku+"','"+judul_buku+"','"+penulis_buku+"','"+penerbit_buku+"', '"+tahun_penerbit+"' ,'"+stok+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('buku'))

@application.route('/updatebuku', methods=["POST"])
def updatebuku():
    id_buku = request.form['id_buku']
    kode_buku = request.form['kode_buku']
    judul_buku = request.form['judul_buku']
    penulis_buku = request.form['penulis_buku']
    penerbit_buku = request.form['penerbit_buku']
    tahun_penerbit = request.form['tahun_penerbit']
    stok = request.form['stok']
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("UPDATE buku SET kode_buku=%s,judul_buku=%s,penulis_buku=%s,penerbit_buku=%s,tahun_penerbit=%s,stok=%s WHERE id_buku=%s",(kode_buku,judul_buku,penulis_buku,penerbit_buku,tahun_penerbit,stok,id_buku,))
    db.commit()
    return redirect(url_for('buku'))

@application.route('/hapusbuku/<string:id_buku>', methods=["GET"])
def hapusbuku(id_buku):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("DELETE FROM buku WHERE id_buku=%s", (id_buku,))
    db.commit()
    return redirect(url_for('buku'))

@application.route('/')
@application.route('/peminjaman')
def peminjaman():
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from peminjaman"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('peminjaman.html', kalimat=output_json)

@application.route('/peminjaman', methods=['GET','POST'])
def simpanpeminjaman():
    print(request.method)
    if request.method == 'GET':
        return render_template('peminjaman.html')
    else: 
        request.method == 'POST'
        tanggal_pinjam = request.form['tanggal_pinjam']
        tanggal_kembali = request.form['tanggal_kembali']
        id_buku = request.form['id_buku']
        id_anggota = request.form['id_anggota']
        id_petugas = request.form['id_petugas']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO peminjaman (tanggal_pinjam, tanggal_kembali, id_buku, id_anggota, id_petugas) VALUES ('"+tanggal_pinjam+"','"+tanggal_kembali+"','"+id_buku+"', '"+id_anggota+"' ,'"+id_petugas+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('peminjaman'))

@application.route('/tambahpinjam', methods=['GET','POST'])
def tambahpinjam():
    print(request.method)
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "SELECT id_buku , judul_buku FROM `buku`"
            print(sqlstr)
            cur.execute(sqlstr)
            data_buku = cur.fetchall()

            sqlstr = "SELECT id_anggota FROM `anggota`"
            print(sqlstr)
            cur.execute(sqlstr)
            data_anggota = cur.fetchall()

            sqlstr = "SELECT id_petugas FROM `petugas`"
            print(sqlstr)
            cur.execute(sqlstr)
            data_petugas = cur.fetchall()

            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
        return render_template('tambahpinjam.html', data_buku=data_buku, data_anggota=data_anggota, data_petugas=data_petugas)
    else: 
        request.method == 'POST'
        tanggal_pinjam = request.form['tanggal_pinjam']
        tanggal_kembali = request.form['tanggal_kembali']
        id_buku = request.form['id_buku']
        id_anggota = request.form['id_anggota']
        id_petugas = request.form['id_petugas']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO peminjaman (tanggal_pinjam, tanggal_kembali, id_buku, id_anggota, id_petugas) VALUES ('"+tanggal_pinjam+"','"+tanggal_kembali+"','"+id_buku+"', '"+id_anggota+"' ,'"+id_petugas+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('peminjaman'))

@application.route('/updatepeminjaman', methods=["POST"])
def updatepeminjaman():
    id_peminjaman = request.form['id_peminjaman']
    tanggal_pinjam = request.form['tanggal_pinjam']
    tanggal_kembali = request.form['tanggal_kembali']
    id_buku = request.form['id_buku']
    id_anggota = request.form['id_anggota']
    id_petugas = request.form['id_petugas']
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("UPDATE peminjaman SET tanggal_pinjam=%s,tanggal_kembali=%s,id_buku=%s,id_anggota=%s,id_petugas=%s WHERE id_peminjaman=%s",(tanggal_pinjam,tanggal_kembali,id_buku,id_anggota,id_petugas,id_peminjaman,))
    db.commit()
    return redirect(url_for('peminjaman'))

@application.route('/hapuspeminjaman/<string:id_peminjaman>', methods=["GET"])
def hapuspeminjaman(id_peminjaman):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("DELETE FROM peminjaman WHERE id_peminjaman=%s", (id_peminjaman,))
    db.commit()
    return redirect(url_for('peminjaman'))

@application.route('/')
@application.route('/pengembalian')
def pengembalian():
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from pengembalian"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('pengembalian.html', kalimat=output_json)

@application.route('/pengembalian', methods=['GET','POST'])
def simpanpengembalian():
    print(request.method)
    if request.method == 'GET':
        return render_template('pengembalian.html')
    else: 
        request.method == 'POST'
        tanggal_pengembalian= request.form['tanggal_pengembalian']
        denda= request.form['denda']
        id_buku = request.form['id_buku']
        id_anggota = request.form['id_anggota']
        id_petugas = request.form['id_petugas']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO pengembalian (tanggal_pengembalian, denda, id_buku, id_anggota, id_petugas) VALUES ('"+tanggal_pengembalian+"','"+denda+"','"+id_buku+"', '"+id_anggota+"' ,'"+id_petugas+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('pengembalian'))

@application.route('/tambahpengembalian', methods=['GET','POST'])
def tambahpengembalian():
    print(request.method)
    if request.method == 'GET':
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "SELECT id_buku , judul_buku FROM `buku`"
            print(sqlstr)
            cur.execute(sqlstr)
            data_buku = cur.fetchall()

            sqlstr = "SELECT id_anggota FROM `anggota`"
            print(sqlstr)
            cur.execute(sqlstr)
            data_anggota = cur.fetchall()

            sqlstr = "SELECT id_petugas FROM `petugas`"
            print(sqlstr)
            cur.execute(sqlstr)
            data_petugas = cur.fetchall()

            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
        return render_template('tambahpengembalian.html', data_buku=data_buku, data_anggota=data_anggota, data_petugas=data_petugas)
    else: 
        request.method == 'POST'
        tanggal_pengembalian = request.form['tanggal_kembali']
        id_buku = request.form['id_buku']
        id_anggota = request.form['id_anggota']
        id_petugas = request.form['id_petugas']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO peminjaman (tanggal_pinjam, tanggal_kembali, id_buku, id_anggota, id_petugas) VALUES ('"+tanggal_pengembalian+"','"+id_buku+"', '"+id_anggota+"' ,'"+id_petugas+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('pengembalian'))

@application.route('/updatepengembalian', methods=["POST"])
def updatepengembalian():
    id_pengembalian = request.form['id_pengembalian']
    tanggal_pengembalian = request.form['tanggal_pengembalian']
    denda = request.form['denda']
    id_buku = request.form['id_buku']
    id_anggota = request.form['id_anggota']
    id_petugas = request.form['id_petugas']
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("UPDATE pengembalian SET tanggal_pengembalian=%s,denda=%s,id_buku=%s,id_anggota=%s,id_petugas=%s WHERE id_pengembalian=%s",(tanggal_pengembalian,denda,id_buku,id_anggota,id_petugas,id_pengembalian,))
    db.commit()
    return redirect(url_for('pengembalian'))

@application.route('/hapuspengembalian/<string:id_pengembalian>', methods=["GET"])
def hapuspengembalian(id_pengembalian):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("DELETE FROM pengembalian WHERE id_pengembalian=%s", (id_pengembalian,))
    db.commit()
    return redirect(url_for('pengembalian'))

@application.route('/')
@application.route('/petugas')
def petugas():
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from petugas"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('petugas.html', kalimat=output_json)

@application.route('/petugas', methods=['GET','POST'])
def simpanpetugas():
    print(request.method)
    if request.method == 'GET':
        return render_template('petugas.html')
    else: 
        request.method == 'POST'
        nama_petugas= request.form['nama_petugas']
        jabatan_petugas = request.form['jabatan_petugas']
        no_telp_petugas = request.form['no_telp_petugas']
        alamat_petugas = request.form['alamat_petugas']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO petugas (nama_petugas, jabatan_petugas, no_telp_petugas, alamat_petugas) VALUES ('"+nama_petugas+"','"+jabatan_petugas+"', '"+no_telp_petugas+"' ,'"+alamat_petugas+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('petugas'))

@application.route('/updatepetugas', methods=["POST"])
def updatepetugas():
    id_petugas = request.form['id_petugas']
    nama_petugas = request.form['nama_petugas']
    jabatan_petugas = request.form['jabatan_petugas']
    no_telp_petugas = request.form['no_telp_petugas']
    alamat_petugas = request.form['alamat_petugas']
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("UPDATE petugas SET nama_petugas=%s,jabatan_petugas=%s,no_telp_petugas=%s,alamat_petugas=%s WHERE id_petugas=%s",(nama_petugas,jabatan_petugas,no_telp_petugas,alamat_petugas,id_petugas,))
    db.commit()
    return redirect(url_for('petugas'))

@application.route('/hapuspetugas/<string:id_petugas>', methods=["GET"])
def hapuspetugas(id_petugas):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("DELETE FROM petugas WHERE id_petugas=%s", (id_petugas,))
    db.commit()
    return redirect(url_for('petugas'))

@application.route('/')
@application.route('/rak')
def rak():
    db = getMysqlConnection()
    try:
        sqlstr = "SELECT * from rak"
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return render_template('rak.html', kalimat=output_json)

@application.route('/rak', methods=['GET','POST'])
def simpanrak():
    print(request.method)
    if request.method == 'GET':
        return render_template('rak.html')
    else: 
        request.method == 'POST'
        nama_rak= request.form['nama_rak']
        lokasi_rak = request.form['lokasi_rak']
        id_buku = request.form['id_buku']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO rak (nama_rak, lokasi_rak, id_buku) VALUES ('"+nama_rak+"','"+lokasi_rak+"', '"+id_buku+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('rak'))

@application.route('/updaterak', methods=["POST"])
def updaterak():
    id_rak = request.form['id_rak']
    nama_rak = request.form['nama_rak']
    lokasi_rak = request.form['lokasi_rak']
    id_buku = request.form['id_buku']
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("UPDATE rak SET nama_rak=%s,lokasi_rak=%s,id_buku=%s WHERE id_rak=%s",(nama_rak,lokasi_rak,id_buku,id_rak,))
    db.commit()
    return redirect(url_for('rak'))

@application.route('/hapusrak/<string:id_rak>', methods=["GET"])
def hapusrak(id_rak):
    db = getMysqlConnection()
    cur = db.cursor()
    cur.execute("DELETE FROM rak WHERE id_rak=%s", (id_rak,))
    db.commit()
    return redirect(url_for('rak'))

@application.route('/register', methods=['GET','POST'])
def register():
    print(request.method)
    if request.method == 'GET':
        return render_template('register.html')
    else: 
        request.method == 'POST'
        username = request.form['username']
        password = request.form['password']
        db = getMysqlConnection()
        try:
            cur = db.cursor()
            sukses = "Data Berhasil Ditambahkan"
            sqlstr = "INSERT INTO register (username , password) VALUES ('"+username+"','"+password+"')"
            print(sqlstr)
            cur.execute(sqlstr)
            db.commit()
            cur.close()
        except Exception as e:
            print('Error in SQL:\n', e)
        finally:
            db.close()
            return redirect(url_for('login'))

@application.route('/login', methods=['GET','POST'])
def login():
    print(request.method)
    if request.method == 'GET':
        return render_template('login.html')
    else: 
        request.method == 'POST'
        username = request.form['username']
        password = request.form['password']
        db = getMysqlConnection()
        try:
            sqlstr = "SELECT * from register WHERE username='"+username+"'"
            cur = db.cursor()
            cur.execute(sqlstr)
            data = cur.fetchone()
            output_json = cur.fetchall()
            
        except Exception as e:
            print("Error in SQL:\n", e)
        finally:
            db.close()
        if data == None :            
            return redirect(url_for('login'))
        else : 
            if data[1]== password : 
                return render_template('dashboard.html')
            else : 
                return redirect(url_for('login'))
    

       

if __name__ == '__main__':
    application.run(debug=True)