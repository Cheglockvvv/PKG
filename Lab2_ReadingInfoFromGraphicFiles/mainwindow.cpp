#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QImageWriter>
#include <QDir>
#include <QFileInfo>
#include <QImage>
#include <QHeaderView>


MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    provider = new QFileSystemModel(this);
    provider->setFilter(QDir::AllEntries);
    provider->setRootPath("");
    info = new QTableWidget;
    info->setStyleSheet("background-color: white");
    ui->horizontalLayout_4->addWidget(info);
    info->setColumnCount(5);
    info->setEditTriggers(QAbstractItemView::NoEditTriggers);
    info->setHorizontalHeaderItem(0, new QTableWidgetItem("Имя файла"));
    info->setHorizontalHeaderItem(1, new QTableWidgetItem("Размер изображения"));
    info->setHorizontalHeaderItem(2, new QTableWidgetItem("Разрешение"));
    info->setHorizontalHeaderItem(3, new QTableWidgetItem("Глубина цвета"));
    info->setHorizontalHeaderItem(4, new QTableWidgetItem("Сжатие"));
    info->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
    connect(ui->OpenFileButton, SIGNAL(clicked(bool)), this, SLOT(OpenFile()));
    connect(ui->ProviderButton, SIGNAL(clicked(bool)), this, SLOT(ProviderChoice()));
}

void MainWindow::addToTable(const QString &fileName, const QString &size, const QString &resolution, const QString &colorDepth, const QString &compression)
{
    int row = info->rowCount();
    info->insertRow(row);
    info->setItem(row, 0, new QTableWidgetItem(fileName));
    info->setItem(row, 1, new QTableWidgetItem(size));
    info->setItem(row, 2, new QTableWidgetItem(resolution));
    info->setItem(row, 3, new QTableWidgetItem(colorDepth));
    info->setItem(row, 4, new QTableWidgetItem(compression));
}

void MainWindow::addImageToTable(const QString &imagePath)
{
    QFileInfo fileInfo(imagePath);
    QImage image(imagePath);

    double compressionRatio = calculateCompressionRatio(image.size(), fileInfo.size());
    QString colorDepth = image.format() == QImage::Format_Indexed8 ? "8 bits" : "32 bits";

    int row = info->rowCount();
    info->insertRow(row);
    info->setItem(row, 0, new QTableWidgetItem(fileInfo.fileName()));
    info->setItem(row, 1, new QTableWidgetItem(QString("%1x%2").arg(image.size().width()).arg(image.size().height()))); //size
    info->setItem(row, 2, new QTableWidgetItem(QString::number(image.physicalDpiX()) + " DPI")); //resolution
    info->setItem(row, 3, new QTableWidgetItem(colorDepth)); //color depth
    info->setItem(row, 4, new QTableWidgetItem(QString::number(compressionRatio))); //compression
}

void MainWindow::ProviderChoice()
{
    QString folderPath = QFileDialog::getExistingDirectory(this, "Выберите папку с изображениями");

    if (folderPath.isNull() || folderPath.isEmpty())
    {
        return;
    }

    provider->setRootPath(folderPath);
    QDir directory(folderPath);
    QStringList imageFilters;
    imageFilters << "*.jpg" << "*.jpeg" << "*.png" << "*.gif" << "*.bmp" << "*.tiff";
    QStringList imageFiles = directory.entryList(imageFilters, QDir::Files);

    for (const QString &filename : imageFiles)
    {
        QString imagePath = directory.filePath(filename);
        addImageToTable(imagePath);
    }
}

void MainWindow::OpenFile()
{
    QString filePath = QFileDialog::getOpenFileName(this, "Открыть изображение", "", "Images (*.png *.jpg *.bmp);;All files (*.*)");

    if (!filePath.isEmpty())
    {
        QFileInfo fileInfo(filePath);
        QImageWriter a(filePath);
        QImage img(filePath);

        QString resolution = fileInfo.suffix();
        if (resolution == "jpg" || resolution == "JPG" || resolution == "gif" || resolution == "tif" || resolution == "bmp" ||
            resolution == "png" || resolution == "pcx" || resolution == "BMP")
        {
            double compressionRatio = calculateCompressionRatio(img.size(), fileInfo.size());
            addToTable(fileInfo.fileName(), QString("%1x%2").arg(img.size().width()).arg(img.size().height()), QString::number(img.physicalDpiX()) + " DPI", QString::number(img.bitPlaneCount()) + " bits",QString::number(compressionRatio));
        }
    }
}

double MainWindow::calculateCompressionRatio(const QSize &imageSize, qint64 fileSize)
{
    double resolutionFactor = imageSize.width() * imageSize.height();
    double compressionRatio = resolutionFactor / fileSize;
    return compressionRatio;
}

MainWindow::~MainWindow()
{
    delete ui;
}


