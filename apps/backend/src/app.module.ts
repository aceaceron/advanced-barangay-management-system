import { Module } from '@nestjs/common';
import { AuthModule } from './modules/auth/auth.module';
import { ResidentsModule } from './modules/residents/residents.module';
import { GisModule } from './modules/gis/gis.module';
import { AppController } from './app.controller';

@Module({
  imports: [AuthModule, ResidentsModule, GisModule],
  controllers: [AppController],
})
export class AppModule {}
