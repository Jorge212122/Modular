// inicioApp.dart
import 'package:flutter/material.dart';
import 'interfazTutorias.dart';
import 'interfazAgenda.dart'; 

class InicioApp extends StatelessWidget {
  final int userId;

  InicioApp({required this.userId});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Inicio'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.count(
          crossAxisCount: 2, // Número de columnas en la cuadrícula
          crossAxisSpacing: 10.0,
          mainAxisSpacing: 10.0,
          children: <Widget>[
            _buildGridButton(context, 'Tutorias Disponibles', Icons.school, () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => InterfazTutorias(userId: userId)),
              );
            }),
            _buildGridButton(context, 'Mi Agenda', Icons.calendar_today, () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => AgendaScreen(userId: userId)),
              );
            }),
            _buildGridButton(context, 'Solicitudes Pendientes', Icons.safety_divider, () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => AgendaScreen(userId: userId)),
              );
            }),
            _buildGridButton(context, 'Mis Tutorias', Icons.book, () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => AgendaScreen(userId: userId)),
              );
            }),
          ],
        ),
      ),
    );
  }

  Widget _buildGridButton(BuildContext context, String title, IconData icon, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        decoration: BoxDecoration(
          color: Colors.blue[800], // Azul rey
          borderRadius: BorderRadius.circular(8.0),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Icon(icon, color: Colors.white, size: 50.0),
            SizedBox(height: 10.0),
            Text(
              title,
              style: TextStyle(color: Colors.white, fontSize: 18.0),
              textAlign: TextAlign.center,
            ),
          ],
        ),
      ),
    );
  }
}
