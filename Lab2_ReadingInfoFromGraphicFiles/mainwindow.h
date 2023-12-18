
#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QFileSystemModel>
#include <QTableWidget>
#include <QFileDialog>


QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow

{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void ProviderChoice();
    void OpenFile();
    void addImageToTable(const QString &imagePath);
    void addToTable(const QString &fileName, const QString &size, const QString &resolution, const QString &colorDepth, const QString &compression);

private:
    Ui::MainWindow *ui;
    void addItemToTable(const QString &fileName, const QString &size, const QString &resolution, const QString &colorDepth, const QString &compression);
    QFileSystemModel *provider;
    QTableWidget *info;
    double calculateCompressionRatio(const QSize &imageSize, qint64 fileSize);
};

#endif // MAINWINDOW_H
